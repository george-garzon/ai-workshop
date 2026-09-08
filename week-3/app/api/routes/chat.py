# app/api/routes/chat.py
from fastapi import HTTPException
from app.schemas import ChatRequest
from app.services import asyncopenai
from app.services.cruise_service import document_search_by_id, document_search
from app.services.ingestion import extract_document_text, ingest_document, extract_pdf_text


def health():
    return {"ok": "200"}

async def chat(request: ChatRequest):
    try:
        instructions = request.instructions
        question = request.question

        if not instructions or not question:
            raise HTTPException(
                status_code=400,
                detail="Invalid Chat Request"
            )

        # Setup wiring to OpenAI Service to process document search
        response = await asyncopenai(
            instructions=instructions,
            question=question,
        )

        # usage = response["usage"]

        return response

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

async def document_by_id(document_id: int):
    document_data = await document_search_by_id(document_id)
    pdf_url = document_data["url"]

    text = await extract_pdf_text(pdf_url)

    return await ingest_document(document_id, text)

async def document():
    document_data = await document_search()
    return document_data
