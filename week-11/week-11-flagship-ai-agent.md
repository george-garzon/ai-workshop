# Week 11 — Flagship AI Agent Project

## Goal
Build a second portfolio project that solves a real business workflow instead of another generic chatbot.

## Project #2 — Business Workflow AI Agent

A strong example is an AI travel/cruise assistant.

### Example User Request
> Find a Caribbean cruise for two adults and one child in November. Budget is $4,000. Prefer Royal Caribbean and a balcony.

### Workflow
1. Extract structured requirements
2. Validate missing/invalid information
3. Search structured inventory
4. Retrieve relevant policies with RAG
5. Compare itineraries
6. Compare ships/options
7. Calculate or retrieve pricing
8. Explain tradeoffs
9. Produce structured recommendations
10. Request human approval where needed

## Architecture
```text
                 User
                   ↓
                Next.js
                   ↓
                FastAPI
                   ↓
               LangGraph
          ↙         ↓        ↘
     Search/API     RAG       MCP/tools
          ↘         ↓        ↙
                AI workflow
                   ↓
          Structured recommendation
```

## Demonstrate
Your project should ideally show:
- LLM APIs
- Structured outputs
- Tool calling
- Agents/workflows
- RAG
- Embeddings/vector search
- MCP
- APIs
- Databases
- FastAPI
- Next.js
- Docker
- Security controls
- Evals/observability

## Checkpoint
The project should look like software a company could deploy—not an AI tutorial.
