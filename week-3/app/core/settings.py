# app/core/settings.py
from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

PROJECT_DIR = Path(__file__).resolve().parents[2]

class Settings(BaseSettings):
    # App
    app_name: str = "Week 3 LLM API"
    environment: str = "development"
    debug: bool = True

    # Open AI
    openai_api_key: str
    openai_model: str = "gpt-5-mini"

    # Backend Cruise API
    backend_api_url: str
    backend_api_secret_key: str
    backend_api_basic_auth: str

    # LLM Config
    max_output_tokens: int = 1000
    temperature: float = 0.7

    model_config = SettingsConfigDict(
        env_file=PROJECT_DIR / ".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

@lru_cache
def get_settings() -> Settings:
    return Settings()

settings = get_settings()
