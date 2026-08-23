## Week 1 - LLM APIs + Python

- Learn the OpenAI and Anthropic Python SDKs.
- Understand:
  - Messages and system instructions
  - Tokens
  - Context windows
  - Temperature
  - Streaming
- Practice:
  - Error handling
  - Retries
  - Async API calls
  - Pydantic
  - FastAPI integration
  - Secrets management
- **Build:** a FastAPI `POST /chat` endpoint that streams an LLM response.


- useful commands
  - fastapi dev main.py
  - uv add (package)


- Folder Structure
  - **app/api/routes/** — /chat and /health endpoints
  - **app/core/** — settings, secrets, and shared configuration
  - **app/models/** — internal/domain models, if needed
  - **app/schemas/** — Pydantic request and response schemas
  - **app/services/** — OpenAI/Anthropic calls, streaming, retries
  - **tests/** — endpoint and service tests
  - **main.py** — creates the FastAPI app and registers routes