import subprocess
import sys


def test_cli_help():
    result = subprocess.run(
        [sys.executable, "labs/sandbox1.py", "--help"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "Sandbox for quick Eidos experiments" in result.stdout
