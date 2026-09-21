from fastapi import APIRouter, File, HTTPException, UploadFile, status

from app.core.settings import settings
from app.schemas import Conversation, ConversationSummary, MessageRequest
from app.services import ConversationStore, answer_from_pdf

router = APIRouter(prefix="/conversations", tags=["conversations"])
store = ConversationStore(settings.conversation_dir)


def _get_conversation(conversation_id: str) -> Conversation:
    try:
        return store.get(conversation_id)
    except FileNotFoundError as error:
        raise HTTPException(status_code=404, detail=str(error)) from error


@router.post("", response_model=Conversation, status_code=status.HTTP_201_CREATED)
async def create_conversation(file: UploadFile = File(...)) -> Conversation:
    filename = file.filename or "document.pdf"
    if file.content_type != "application/pdf" and not filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=415, detail="A PDF document is required")

    pdf_bytes = await file.read(settings.max_pdf_bytes + 1)
    await file.close()
    if len(pdf_bytes) > settings.max_pdf_bytes:
        raise HTTPException(status_code=413, detail="PDF must be 20 MB or smaller")
    if not pdf_bytes.startswith(b"%PDF-"):
        raise HTTPException(status_code=415, detail="The uploaded file is not a valid PDF")

    return store.create(filename=filename, pdf_bytes=pdf_bytes)


@router.get("", response_model=list[ConversationSummary])
async def list_conversations() -> list[ConversationSummary]:
    return store.list()


@router.get("/{conversation_id}", response_model=Conversation)
async def get_conversation(conversation_id: str) -> Conversation:
    return _get_conversation(conversation_id)


@router.post("/{conversation_id}/messages")
async def create_message(conversation_id: str, request: MessageRequest) -> dict:
    conversation = _get_conversation(conversation_id)
    question = request.message.strip()
    if not question:
        raise HTTPException(status_code=400, detail="Message cannot be empty")

    store.append_message(conversation, "user", question)
    try:
        answer = await answer_from_pdf(conversation, store.pdf_path(conversation))
    except RuntimeError as error:
        raise HTTPException(status_code=503, detail=str(error)) from error
    except Exception as error:
        raise HTTPException(status_code=502, detail=f"OpenAI request failed: {error}") from error

    assistant_message = store.append_message(
        conversation,
        "assistant",
        answer,
        citation=conversation.document.filename,
    )
    return {"conversation_id": conversation.id, "message": assistant_message}
