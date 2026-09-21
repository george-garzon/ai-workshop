# Week 4 backend

FastAPI backend for the PDF knowledge assistant. Every conversation requires one
PDF, stores its document and message history under `data/conversations/`, and
uses the OpenAI Responses API to answer from that document.

## Setup

1. Add `OPENAI_API_KEY` to `.env`.
2. Install dependencies with `uv sync --dev`.
3. Start the API with `uv run fastapi dev app/main.py --port 8000`.
4. Start the frontend from `week-4/frontend/my-app` with `npm run dev`.

The frontend defaults to `http://localhost:8000`. Override it with
`NEXT_PUBLIC_API_URL` in the frontend environment when needed.

Local PDFs and conversation JSON files are deliberately ignored by Git.
