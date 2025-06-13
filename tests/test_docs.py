from pathlib import Path
import subprocess
import sys


def test_core_usage_notebook_executes(tmp_path: Path) -> None:
    """Run the core usage notebook to ensure it executes without error."""
    notebook = Path("docs/core_usage.ipynb")
    assert notebook.exists()
    output = tmp_path / "out.ipynb"
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "jupyter",
            "nbconvert",
            "--to",
            "html",
            "--execute",
            "--output",
            output,
            notebook,
        ],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
