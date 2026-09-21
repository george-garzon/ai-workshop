import base64
from pathlib import Path

from openai import AsyncOpenAI

from app.core.settings import settings
from app.schemas import Conversation


def _pdf_data_url(pdf_path: Path) -> str:
    encoded = base64.b64encode(pdf_path.read_bytes()).decode("ascii")
    return f"data:application/pdf;base64,{encoded}"


def _response_input(conversation: Conversation, pdf_path: Path) -> list[dict]:
    conversation_history: list[dict] = [
        {
            "role": "user",
            "content": [
                {
                    "type": "input_file",
                    "filename": conversation.document.filename,
                    "file_data": _pdf_data_url(pdf_path),
                },
                {
                    "type": "input_text",
                    "text": "This PDF is the only document you may use for this conversation.",
                },
            ],
        }
    ]
    conversation_history.extend(
        {"role": message.role, "content": message.text}
        for message in conversation.messages
    )
    return conversation_history


async def answer_from_pdf(conversation: Conversation, pdf_path: Path) -> str:
    if not settings.openai_api_key:
        raise RuntimeError("OPENAI_API_KEY is missing from week-4/backend/.env")

    instructions = settings.chatbot_context_file.read_text(encoding="utf-8")
    async with AsyncOpenAI(
        api_key=settings.openai_api_key,
        max_retries=3,
        timeout=90.0,
    ) as client:
        response = await client.responses.create(
            model=settings.openai_model,
            instructions=instructions,
            input=_response_input(conversation, pdf_path),
            max_output_tokens=settings.max_output_tokens,
            store=False,
        )
    return response.output_text.strip()
