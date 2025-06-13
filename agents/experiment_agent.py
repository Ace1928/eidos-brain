"""Agent dedicated to running experiments within Eidos-Brain."""

from __future__ import annotations

from .agent import Agent


class ExperimentAgent(Agent):
    """Handles experimental cycles and evaluations."""

    def run(self, hypothesis: str) -> str:
        """Execute an experiment and return its result."""
        return f"Experimenting with {hypothesis}"

    def run_series(self, hypotheses: list[str]) -> list[str]:
        """Run a series of experiments and collect results."""
        return [self.run(h) for h in hypotheses]
