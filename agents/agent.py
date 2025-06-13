"""Base interface for all Eidos agents."""

from __future__ import annotations

from abc import ABC, abstractmethod


class Agent(ABC):
    """Define the minimal interface required for Eidos agents."""

    @abstractmethod
    def run(self, *args, **kwargs) -> object:
        """Execute the agent's primary behavior."""
        raise NotImplementedError
