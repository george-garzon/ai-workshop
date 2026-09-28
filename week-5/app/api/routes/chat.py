from fastapi import HTTPException

from app.schemas import AgentRunRequest
from app.services import run_agent


async def chat(request: AgentRunRequest):
    if not request.instructions or not request.question:
        raise HTTPException(
            status_code=400,
            detail="Invalid agent request",
        )

    try:
        return await run_agent(request)
    except NotImplementedError as exc:
        raise HTTPException(
            status_code=501,
            detail=str(exc),
        ) from exc
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=str(exc),
        ) from exc


def health():
    return {"ok": "200"}
