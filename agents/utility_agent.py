"""General-purpose utilities for Eidos."""

from __future__ import annotations

from datetime import datetime
from pathlib import Path


class UtilityAgent:
    """Provides supporting functions for the system."""

    def perform_task(self, task: str) -> str:
        """Perform a simple utility task and return a status message."""
        return f"Performed {task}"

    def current_timestamp(self) -> str:
        """Return the current UTC timestamp in ISO-8601 format."""
        return datetime.utcnow().isoformat()

    def log_with_timestamp(self, message: str, file_path: str | None = None) -> str:
        """Return ``message`` prefixed with a timestamp and optionally log it.

        Parameters
        ----------
        message:
            Text to record in the log.
        file_path:
            Optional path to a file where the log line should be appended.

        Returns
        -------
        str
            The full timestamped log line.
        """
        line = f"[{self.current_timestamp()}] {message}"
        if file_path:
            path = Path(file_path)
            with path.open("a", encoding="utf-8") as handle:
                handle.write(line + "\n")
        return line
