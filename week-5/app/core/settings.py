"""Exercise 2: load configuration in one place.

Purpose
-------
Settings turn environment variables into typed Python values. Other modules
should ask this module for configuration instead of repeatedly reading .env.
This keeps the model name and execution limits consistent throughout a run.

Build it yourself
-----------------
1. Add the fields described in Settings below, with type hints and defaults.
2. Use SettingsConfigDict to read .env as UTF-8, match environment names without
   case sensitivity, and ignore unrelated entries in that file.
3. Give both numeric limits a positive-value constraint (for example, through
   Pydantic Field). Zero or negative limits should fail configuration validation.
4. Implement get_settings. After it works, consider functools.lru_cache so
   repeated calls reuse one Settings instance. Clear that cache in tests that
   change the environment.
5. Call get_settings when a service needs it. Avoid constructing settings or
   an API client at module import time: offline exercises and /health should
   remain usable without credentials.

Check your work
---------------
Supply settings explicitly in a small local check. Verify an environment value
such as MAX_AGENT_ITERATIONS=3 becomes an integer, and a negative limit fails.
Never print the API key to check that it loaded. .env is resolved relative to
your working directory; use week-5 as the working directory for this project.
"""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """TODO: define the configuration contract.

    Fields to add:
    - app_name: string identifying this app; choose a descriptive default.
    - environment: string, default "development".
    - debug: boolean, default True for this local exercise.
    - openai_api_key: required string when loading live-model configuration.
    - openai_model: string; match the model configured in .env.example.
    - max_output_tokens: positive integer, suggested default 1000.
    - max_agent_iterations: positive integer, suggested default 5.

    This empty model is only a placeholder; it does not validate these yet.
    """

    pass


def get_settings() -> Settings:
    """TODO: construct and return validated settings, then add caching if useful."""
    raise NotImplementedError("Exercise 2: implement configuration loading.")
