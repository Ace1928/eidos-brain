"""Agent dedicated to running experiments within Eidos-Brain."""


class ExperimentAgent:
    """Handles experimental cycles and evaluations."""

    def __init__(self) -> None:
        """Initialize a fresh experiment log."""
        self.log: list[str] = []

    def run(self, hypothesis: str) -> str:
        """Run an experimental cycle with ``hypothesis`` and log progress.

        The method records each step in :attr:`log`, starting with the
        provided hypothesis and ending with the outcome message.

        Parameters
        ----------
        hypothesis:
            Description of the idea to test.

        Returns
        -------
        str
            Message summarizing the experiment result.
        """
        self.log.append(f"start:{hypothesis}")
        outcome = f"Experimenting with {hypothesis}"
        self.log.append(f"complete:{outcome}")
        return outcome
