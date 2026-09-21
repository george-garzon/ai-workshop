export type WorkshopArticle = {
  week: number;
  title: string;
  summary: string;
  concepts: string[];
  accomplishment: string;
  steps: string[];
};

export const workshopArticles: WorkshopArticle[] = [
  {
    week: 1,
    title: "LLM APIs, streaming, and FastAPI",
    summary: "Learn how an application talks to language models reliably and streams responses as they are generated.",
    concepts: ["Messages and system instructions", "Tokens, context windows, and temperature", "Async streaming", "Pydantic validation", "Retries, errors, and secrets management"],
    accomplishment: "We built a FastAPI POST /chat endpoint that accepts validated JSON and streams an OpenAI response to the client.",
    steps: ["Separated routes, schemas, settings, and model services", "Moved API keys into application settings", "Handled missing keys, timeouts, rate limits, and API errors", "Tested health checks, valid chat requests, and invalid inputs"],
  },
  {
    week: 2,
    title: "Structured output and tool calling",
    summary: "Move beyond free-form chat by letting a model request safe, validated application actions.",
    concepts: ["Structured JSON outputs", "Pydantic response schemas", "Tool selection and arguments", "Parallel tool calls", "Deterministic workflows versus agents"],
    accomplishment: "We built a cruise-search assistant that chooses application tools, searches real sailing data, and formats matching results for the user.",
    steps: ["Defined tool schemas the model could understand", "Validated every argument before execution", "Kept authentication and authorization in application code", "Returned results to the model for a clear final answer", "Reported token usage for cost monitoring"],
  },
  {
    week: 3,
    title: "Embeddings and vector search",
    summary: "Represent meaning as vectors and retrieve relevant text by semantic similarity instead of exact words alone.",
    concepts: ["Embeddings and vector dimensions", "Cosine similarity", "Chunk size and overlap", "Similarity thresholds", "PostgreSQL and pgvector", "Document metadata"],
    accomplishment: "We built a document-ingestion and semantic-search pipeline without hiding retrieval behind an AI framework.",
    steps: ["Extracted and split document text into chunks", "Generated and stored embeddings in pgvector", "Embedded user queries and ran vector similarity searches", "Stored file, page, owner, and date metadata", "Compared chunk sizes, overlap, result counts, and thresholds"],
  },
  {
    week: 4,
    title: "Building a production RAG system",
    summary: "Connect ingestion, retrieval, reranking, and generation into an evidence-grounded knowledge assistant.",
    concepts: ["RAG architecture", "Hybrid and BM25 search", "Metadata filtering", "Query rewriting and reranking", "Context construction", "Citations and retrieval evaluation", "Document permissions"],
    accomplishment: "We started an enterprise knowledge assistant with a Next.js support messenger backed by a FastAPI, PostgreSQL, and pgvector architecture.",
    steps: ["Designed PDF and DOCX ingestion", "Planned parsing, chunking, embeddings, and vector storage", "Designed cited answers and streaming conversations", "Created this responsive onsite support experience", "Prepared the UI to connect to the RAG API"],
  },
];
