import math

from app.services.embeddings import create_embedding
from app.services.ingestion import store


def _cosine_similarity(left: list[float], right: list[float]) -> float:
    dot_product = sum(a * b for a, b in zip(left, right))
    left_norm = math.sqrt(sum(value * value for value in left))
    right_norm = math.sqrt(sum(value * value for value in right))

    if left_norm == 0 or right_norm == 0:
        return 0.0

    return dot_product / (left_norm * right_norm)


def find_chunks(question: str, document_id: int, limit: int = 5) -> list[str]:
    query_embedding = create_embedding(question).cpu().tolist()

    candidates = (
        (chunk, embedding)
        for chunk, embedding, stored_document_id in zip(
            store.chunks,
            store.embeddings,
            store.document_ids,
        )
        if stored_document_id == document_id
    )

    ranked = sorted(
        candidates,
        key=lambda item: _cosine_similarity(query_embedding, item[1]),
        reverse=True,
    )

    return [chunk for chunk, _ in ranked[:limit]]
