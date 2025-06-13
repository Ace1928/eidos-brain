"""Shared base interface for all Eidos agents."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List


class Agent(ABC):
    """Base interface declaring common agent behavior."""

    @abstractmethod
    def perform_task(self, task: str) -> str:
        """Perform a single ``task`` and return a status message."""
        raise NotImplementedError

    def batch_perform(self, tasks: List[str]) -> List[str]:
        """Perform multiple tasks via :py:meth:`perform_task`."""
        return [self.perform_task(t) for t in tasks]
