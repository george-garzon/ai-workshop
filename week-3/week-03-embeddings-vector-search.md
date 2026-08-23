# Week 3 — Embeddings + Vector Search

## Goal
Understand and implement semantic retrieval without hiding everything behind an AI framework.

## Learn
- Embeddings
- Vector dimensions
- Cosine similarity
- Semantic search
- Chunking strategies
- Chunk overlap
- Metadata
- Similarity thresholds
- PostgreSQL
- pgvector

## Build
Create a document-ingestion and search pipeline.

```text
Document
  ↓
Extract text
  ↓
Chunk text
  ↓
Generate embeddings
  ↓
PostgreSQL + pgvector
  ↓
User query embedding
  ↓
Vector similarity search
  ↓
Relevant chunks
```

Store useful metadata with every chunk, such as:
- Document ID
- File name
- Page/section
- Owner/user
- Created date

## Experiments
Compare:
- Small vs. large chunks
- Different overlap sizes
- Top 3 vs. top 10 retrieval
- Different similarity thresholds

## Checkpoint
You should be able to:
- Explain what embeddings represent
- Explain cosine similarity
- Store/query vectors with pgvector
- Explain why chunking affects retrieval quality
- Write vector-search queries rather than relying entirely on framework abstractions
