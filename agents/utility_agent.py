"""General-purpose utilities for Eidos."""

from core.event_bus import EventBus


class UtilityAgent:
    """Provides supporting functions for the system."""

    def register(self, bus: "EventBus") -> None:
        """Attach this agent's handlers to ``bus``."""
        bus.subscribe("utility_task", self.perform_task)

    def perform_task(self, task: str) -> str:
        """Perform a simple utility task and return a status message."""
        return f"Performed {task}"

    def batch_perform(self, tasks: list[str]) -> list[str]:
        """Perform multiple tasks and collect status messages."""
        return [self.perform_task(t) for t in tasks]
