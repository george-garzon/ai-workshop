# app/api/routes/chat.py
from logging import exception

from app.schemas import ChatRequest
from app.services import asyncopenai
from fastapi import HTTPException

async def chat(request: ChatRequest):
    try:
        instructions = request.instructions
        question = request.question

        if not instructions or not question:
            raise HTTPException(
                status_code=400,
                detail="Invalid Chat Request"
            )

        response = await asyncopenai(instructions,question)

        usage = response["usage"]

        return {
            "response": response["response"],
            "usage": {
                "input_tokens": usage.input_tokens,
                "cached_tokens": usage.input_tokens_details.cached_tokens,
                "output_tokens": usage.output_tokens,
                "reasoning_tokens": usage.output_tokens_details.reasoning_tokens,
                "total_tokens": usage.total_tokens,
            },
        }

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

def health():
    return {"ok": "200"}