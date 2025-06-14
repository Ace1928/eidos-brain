"""General-purpose utilities for Eidos."""


class UtilityAgent:
    """Provides supporting functions for the system."""

    def perform_task(self, task: str) -> str:
        """Perform a simple utility task and return a status message.

        Parameters
        ----------
        task : str
            Name of the task to perform.

        Returns
        -------
        str
            Confirmation message describing the performed task.
        """
        return f"Performed {task}"

    def batch_perform(self, tasks: list[str]) -> list[str]:
        """Perform multiple tasks and collect status messages."""
        return [self.perform_task(t) for t in tasks]
