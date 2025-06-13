import subprocess
import sys


def test_mutation_cli_help() -> None:
    """Ensure the mutation testing CLI is accessible."""
    result = subprocess.run(
        [sys.executable, "tools/mutation_test.py", "--help"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "mutation tests" in result.stdout
