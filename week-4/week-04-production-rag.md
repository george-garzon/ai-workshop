# Week 4 — Production RAG

## Goal
Build a complete Retrieval-Augmented Generation pipeline.

## Learn
- RAG architecture
- Hybrid search
- Keyword/BM25 search
- Metadata filtering
- Reranking
- Query rewriting
- Context construction
- Citations
- Retrieval evaluation
- Document permissions

## Project #1 — Enterprise Knowledge Assistant
Start your first flagship project.

### Suggested Stack
- Next.js
- TypeScript
- Python
- FastAPI
- PostgreSQL
- pgvector
- OpenAI and/or Anthropic
- Docker

### Features
- Authentication
- PDF/document upload
- Document parsing
- Chunking
- Embeddings
- Vector storage
- Semantic retrieval
- Reranking
- Chat with documents
- Citations
- Streaming responses
- Conversation history

## Architecture
```text
PDF / DOCX
    ↓
Parser
    ↓
Chunking
    ↓
Embeddings
    ↓
PostgreSQL + pgvector
    ↓
Retrieval
    ↓
Reranking
    ↓
LLM
    ↓
Answer + citations
```

## Checkpoint
You should be able to:
- Explain the complete RAG pipeline
- Explain RAG vs. sending an entire document to an LLM
- Implement metadata filtering
- Generate answers grounded in retrieved evidence
- Return useful citations
