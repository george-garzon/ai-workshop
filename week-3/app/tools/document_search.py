# app/tools/document_search.py
import asyncio

from app.models.document import DocumentByIdArgs
from app.services.cruise_service import (
    document_chunk_search,
    document_search,
    document_search_by_id,
)
from app.services.ingestion import (
    extract_pdf_text,
    hydrate_document_chunks,
    ingest_document,
    store,
)
from app.services.retrieval import find_chunks


async def fetch_document_by_id(args: DocumentByIdArgs):
    if args.document_id not in store.document_ids:
        persisted_chunks = []
        limit = 100
        offset = 0

        while True:
            page = await document_chunk_search(
                document_id=args.document_id,
                limit=limit,
                offset=offset,
            )
            persisted_chunks.extend(page)

            if len(page) < limit:
                break

            offset += limit

        if persisted_chunks:
            hydrate_document_chunks(args.document_id, persisted_chunks)
        else:
            document = await document_search_by_id(
                document_id=args.document_id
            )
            pdf_url = document["url"]
            text = await extract_pdf_text(pdf_url)
            await ingest_document(args.document_id, text)

    chunks = await asyncio.to_thread(
        find_chunks,
        args.query,
        args.document_id,
    )

    return {
        "document_id": args.document_id,
        "relevant_chunks": chunks,
    }

async def fetch_documents():
    documents = await document_search()

    return documents
