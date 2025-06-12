"""Agent dedicated to running experiments within Eidos-Brain."""


class ExperimentAgent:
    """Handles experimental cycles and evaluations."""

    def run(self, hypothesis: str) -> str:
        """Execute an experiment and return its result."""
        return f"Experimenting with {hypothesis}"
