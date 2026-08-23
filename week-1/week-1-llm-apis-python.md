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

1. Create a Pydantic ChatRequest with message, instructions, and model. 
2. Rename open-ai.py to openai_service.py so Python can import it normally. 
3. Make the OpenAI service async and stream chunks instead of printing the final response. 
4. Connect that service to /chat using FastAPI’s StreamingResponse.
5. Move API-key/config handling into app/core/settings.py.
6. Handle missing keys, timeouts, rate limits, and API errors.
7. Add tests for /health, valid chat requests, and invalid inputs.
8. Return {"status": "ok"} from /health; "200" is a status code, not health data.
- To improve your coding, focus on:
  - Python naming: clientopenai → stream_openai_response
  - Type hints and explicit return types
  - Small functions with one responsibility
  - Separating routes, schemas, configuration, and services
  - Testing with mocked API calls
  - Reading tracebacks and debugging before asking an AI for the answer
- A practical next-week schedule:
  - Days 1–2: Pydantic schemas, imports, project structure
  - Day 3: Async OpenAI streaming
  - Day 4: Error handling and configuration
  - Day 5: Tests
  - Days 6–7: Add Anthropic behind the same interface and document usage
- Your Week 1 definition of done should be: a client sends JSON to POST /chat, receives streamed text, secrets stay outside the code, failures return sensible errors, and tests pass.


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