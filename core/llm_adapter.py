"""Simplified adapter for querying a large language model."""

from __future__ import annotations


class LLMAdapter:
    """Provide a lightweight interface to an LLM service."""

    def query(self, prompt: str) -> str:
        """Return a placeholder response for ``prompt``."""
        return f"Suggestion: {prompt}"
