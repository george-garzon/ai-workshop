from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

BACKEND_DIR = Path(__file__).resolve().parents[2]
WEEK_4_DIR = BACKEND_DIR.parent


class Settings(BaseSettings):
    app_name: str = "Week 4 PDF Knowledge Assistant"
    environment: str = "development"
    debug: bool = True

    openai_api_key: str = ""
    openai_model: str = "gpt-5-mini"
    max_output_tokens: int = 1200

    frontend_origin: str = "http://localhost:3000"
    max_pdf_bytes: int = 20 * 1024 * 1024
    conversation_dir: Path = BACKEND_DIR / "data" / "conversations"
    chatbot_context_file: Path = WEEK_4_DIR / "CHATBOT_CONTEXT.md"

    model_config = SettingsConfigDict(
        env_file=BACKEND_DIR / ".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
