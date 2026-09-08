# app/tools/document_search.py
import asyncio

from app.models.document import DocumentByIdArgs
from app.services.cruise_service import document_search, document_search_by_id
from app.services.ingestion import extract_pdf_text, ingest_document, store
from app.services.retrieval import find_chunks


async def fetch_document_by_id(args: DocumentByIdArgs):
    document = await document_search_by_id(
        document_id=args.document_id
    )
    pdf_url = document["url"]

    if args.document_id not in store.document_ids:
        text = await extract_pdf_text(pdf_url)
        await asyncio.to_thread(ingest_document, args.document_id, text)

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
