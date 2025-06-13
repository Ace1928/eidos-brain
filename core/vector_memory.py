"""In-memory store for embeddings enabling similarity search."""

from __future__ import annotations

from typing import Any, Iterable, List, Tuple
import math


class VectorMemory:
    """Store vectors with associated items and perform similarity queries."""

    def __init__(self) -> None:
        """Initialize empty memory."""
        self._data: List[Tuple[List[float], Any]] = []

    def add(self, embedding: Iterable[float], item: Any) -> None:
        """Add ``embedding`` and ``item`` to memory."""
        self._data.append((list(embedding), item))

    def query(self, embedding: Iterable[float], top_k: int = 1) -> List[Any]:
        """Return up to ``top_k`` items most similar to ``embedding``."""
        vector = list(embedding)
        scored = [
            (self._cosine_similarity(vector, stored), item)
            for stored, item in self._data
        ]
        scored.sort(key=lambda x: x[0], reverse=True)
        return [item for _, item in scored[:top_k]]

    @staticmethod
    def _cosine_similarity(a: List[float], b: List[float]) -> float:
        """Return cosine similarity between vectors ``a`` and ``b``."""
        if not a or not b:
            return 0.0
        dot = sum(x * y for x, y in zip(a, b))
        norm_a = math.sqrt(sum(x * x for x in a))
        norm_b = math.sqrt(sum(y * y for y in b))
        if norm_a == 0 or norm_b == 0:
            return 0.0
        return dot / (norm_a * norm_b)
