"""Recursive summarization utilities for memory chunks."""

from __future__ import annotations

from typing import Sequence, Any, List

from .meta_reflection import MetaReflection


class MemorySummarizer:
    """Condense large memories for LLM consumption."""

    def __init__(self, chunk_size: int = 5) -> None:
        self.chunk_size = chunk_size
        self.reflector = MetaReflection()

    def summarize(self, items: Sequence[Any]) -> str:
        """Return a recursive summary string for ``items``."""
        if len(items) <= self.chunk_size:
            analysis = self.reflector.analyze(list(items))
            return analysis.get("summary") or analysis.get("repr")
        chunks: List[Sequence[Any]] = [
            items[i : i + self.chunk_size]  # noqa: E203
            for i in range(0, len(items), self.chunk_size)
        ]
        chunk_summaries = [self.summarize(chunk) for chunk in chunks]
        return self.summarize(chunk_summaries)
