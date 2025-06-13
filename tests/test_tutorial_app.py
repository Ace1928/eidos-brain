from unittest.mock import patch

from labs import tutorial_app
from pathlib import Path
import subprocess
import sys


def test_main_exits_quickly():
    with patch("rich.prompt.Prompt.ask", side_effect=["exit"]):
        tutorial_app.main()


def test_save_and_load_memory(tmp_path: Path):
    memory_file = tmp_path / "mem.txt"
    with patch("rich.prompt.Prompt.ask", side_effect=["add", "hello", "exit"]), patch(
        "rich.console.Console.print"
    ) as mock_print:
        tutorial_app.main(save=str(memory_file))
        save_output = "".join(call.args[0] for call in mock_print.call_args_list)
    assert memory_file.exists()
    assert "Memories saved" in save_output
    with patch("rich.prompt.Prompt.ask", side_effect=["reflect", "exit"]), patch(
        "rich.console.Console.print"
    ) as mock_print:
        tutorial_app.main(load=str(memory_file))
        prints = "".join(call.args[0] for call in mock_print.call_args_list)
    assert "Loaded 1 memories" in prints


def test_cli_help():
    result = subprocess.run(
        [
            sys.executable,
            "labs/tutorial_app.py",
            "--help",
        ],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "Eidos interactive tutorial" in result.stdout
