import asyncio
import json
from typing import Any
from io import BytesIO

import httpx
from pypdf import PdfReader

from app.models import DocumentStore
from app.services.embeddings import create_embeddings
from app.services.cruise_service import create_document_chunk
from app.services.text_splitter import split_text

store = DocumentStore()

TEXT_FIELDS = ("content", "text", "body", "document_text", "file_content")
def extract_document_text(document: Any) -> str:
    """Extract text from the common shapes returned by the document API."""
    if isinstance(document, str):
        return document

    if isinstance(document, list):
        parts = [extract_document_text(item) for item in document]
        return "\n\n".join(part for part in parts if part)

    if isinstance(document, dict):
        for field in TEXT_FIELDS:
            value = document.get(field)
            if isinstance(value, str) and value.strip():
                return value

        for field in ("document", "data", "result"):
            if field in document:
                text = extract_document_text(document[field])
                if text:
                    return text

    raise ValueError(
        "Document API response does not contain a supported text field: "
        f"{', '.join(TEXT_FIELDS)}"
    )



async def extract_pdf_text(pdf_url: str) -> str:
    async with httpx.AsyncClient(follow_redirects=True) as client:
        response = await client.get(pdf_url)
        response.raise_for_status()

    reader = PdfReader(BytesIO(response.content))

    return "\n".join(
        text
        for page in reader.pages
        if (text := page.extract_text())
    )

def _prepare_chunks(text: str) -> tuple[list[str], list[list[float]]]:
    chunks = split_text(text)
    if not chunks:
        raise ValueError("The document contains no text to ingest")

    embeddings = create_embeddings(chunks)
    return chunks, embeddings.cpu().tolist()


def hydrate_document_chunks(
    document_id: int,
    records: list[dict[str, Any]],
) -> int:
    """Load persisted backend chunks into the in-process retrieval store."""
    ordered_records = sorted(
        records,
        key=lambda record: int(record.get("chunk_index", 0)),
    )
    chunks: list[str] = []
    embeddings: list[list[float]] = []

    for record in ordered_records:
        content = record.get("content")
        embedding = record.get("embedding")

        if isinstance(embedding, str):
            embedding = json.loads(embedding)

        if not isinstance(content, str) or not isinstance(embedding, list):
            raise ValueError(
                f"Invalid persisted chunk for document {document_id}"
            )

        chunks.append(content)
        embeddings.append([float(value) for value in embedding])

    store.chunks.extend(chunks)
    store.embeddings.extend(embeddings)
    store.document_ids.extend([document_id] * len(chunks))

    return len(chunks)


async def ingest_document(document_id: int, text: str) -> dict[str, int]:
    chunks, embedding_rows = await asyncio.to_thread(_prepare_chunks, text)

    for chunk_index, (chunk, embedding) in enumerate(
        zip(chunks, embedding_rows)
    ):
        await create_document_chunk({
            "document_id": document_id,
            "chunk_index": chunk_index,
            "content": chunk,
            "embedding": json.dumps(embedding),
        })

    store.chunks.extend(chunks)
    store.embeddings.extend(embedding_rows)
    store.document_ids.extend([document_id] * len(chunks))

    return {
        "document_id": document_id,
        "chunks_ingested": len(chunks),
        "chunks_stored": len(chunks),
        "embedding_dimensions": len(embedding_rows[0]),
    }
