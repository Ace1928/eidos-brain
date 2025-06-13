"""Agent dedicated to running experiments within Eidos-Brain."""


class ExperimentAgent:
    """Handles experimental cycles and evaluations."""

    def run(self, hypothesis: str) -> str:
        """Execute an experiment and return its result.

        Parameters
        ----------
        hypothesis : str
            Statement or question to test.

        Returns
        -------
        str
            Message summarizing the experiment execution.
        """
        return f"Experimenting with {hypothesis}"
