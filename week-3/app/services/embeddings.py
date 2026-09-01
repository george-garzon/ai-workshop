# app/services/embeddings.py

from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def create_embeddings(texts: list[str]):
    return model.encode(
        texts,
        convert_to_tensor=True,
    )


def create_embedding(text: str):
    return model.encode(
        text,
        convert_to_tensor=True,
    )