"""General-purpose utilities for Eidos."""

from .agent import Agent


class UtilityAgent(Agent):
    """Provides supporting functions for the system."""

    def perform_task(self, task: str) -> str:
        """Perform a simple utility task and return a status message."""
        return f"Performed {task}"
