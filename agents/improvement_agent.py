"""Agent that proposes codebase improvements using an LLM."""

from __future__ import annotations

from typing import List

from core.llm_adapter import LLMAdapter


class ImprovementAgent:
    """Use :class:`LLMAdapter` to generate and store suggestions."""

    def __init__(self, llm: LLMAdapter | None = None) -> None:
        self.llm = llm or LLMAdapter()
        self.suggestions: List[str] = []

    def propose(self, text: str) -> str:
        """Return an improvement suggestion for ``text`` and record it."""
        suggestion = self.llm.query(text)
        self.suggestions.append(suggestion)
        return suggestion

    def history(self) -> List[str]:
        """Return a copy of stored suggestions."""
        return list(self.suggestions)
