from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.conversations import router as conversations_router
from app.core.settings import settings

app = FastAPI(title=settings.app_name)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.frontend_origin],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)
app.include_router(conversations_router, prefix="/api")


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": settings.app_name}


@app.get("/api/health")
async def health() -> dict[str, str | bool]:
    return {
        "ok": True,
        "model": settings.openai_model,
        "openai_configured": bool(settings.openai_api_key),
    }
