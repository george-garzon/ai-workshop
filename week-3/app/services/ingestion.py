# ingestion.py       # processes + stores documents
from app.models import DocumentStore
from app.services.embeddings import create_embedding, create_embeddings
from app.services.text_splitter import split_text

store = DocumentStore()

def ingest_document(text: str):
    # 1. Split document
    chunks = split_text(text)

    # 2. Create embeddings for every chunk
    embeddings = create_embeddings(chunks)

    # 3. Store them
    store.chunks.extend(chunks)

    return chunks