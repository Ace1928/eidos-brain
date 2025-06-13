import subprocess
import sys


def test_cli_help():
    result = subprocess.run(
        [sys.executable, "tools/generate_glossary.py", "--help"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "Generate a glossary" in result.stdout
