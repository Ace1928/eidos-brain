"""Adapter to prepare long-context LLM interactions."""

from __future__ import annotations

from typing import Any, Iterable, List

from .meta_reflection import MetaReflection


class LongContextAdapter:
    """Summarize large memories for long-context LLM usage."""

    def __init__(self, chunk_size: int = 20, max_summary_len: int = 200) -> None:
        """Initialize the adapter with chunk and length limits."""
        self.chunk_size = chunk_size
        self.max_summary_len = max_summary_len
        self.reflector = MetaReflection()

    def summarize_chunk(self, memories: Iterable[Any]) -> str:
        """Return a condensed summary for ``memories``."""
        details = [self.reflector.analyze(m) for m in memories]
        lines = [f"{d['type']}: {d['summary'] or d['repr']}" for d in details]
        summary = "; ".join(lines)
        return summary[: self.max_summary_len]

    def summarize(self, memories: List[Any]) -> List[str]:
        """Return summaries for batches of ``memories``."""
        summaries: List[str] = []
        for i in range(0, len(memories), self.chunk_size):
            chunk = memories[i : i + self.chunk_size]
            summaries.append(self.summarize_chunk(chunk))
        return summaries
