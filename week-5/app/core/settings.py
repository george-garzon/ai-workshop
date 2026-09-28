from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Week 5 Agent Fundamentals"
    environment: str = "development"
    debug: bool = True

    openai_api_key: str
    openai_model: str = "gpt-5-mini"

    max_output_tokens: int = 1000
    max_agent_iterations: int = 5

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
