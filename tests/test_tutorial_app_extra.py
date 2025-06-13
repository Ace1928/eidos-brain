from unittest.mock import patch
from pathlib import Path

from labs import tutorial_app


def test_load_memory_no_file(tmp_path: Path) -> None:
    core = tutorial_app.EidosCore()
    file_path = tmp_path / "missing.txt"
    console = tutorial_app.Console(record=True)
    tutorial_app.load_memory(core, file_path, console)
    assert "No memory file" in console.export_text()


def test_load_memory_failure(tmp_path: Path) -> None:
    core = tutorial_app.EidosCore()
    file_path = tmp_path / "err.txt"
    console = tutorial_app.Console(record=True)
    with patch.object(Path, "exists", side_effect=OSError("boom")):
        tutorial_app.load_memory(core, file_path, console)
    assert "Failed to load memory" in console.export_text()


def test_save_memory_failure(tmp_path: Path) -> None:
    core = tutorial_app.EidosCore()
    core.memory.append("data")
    file_path = tmp_path / "err.txt"
    console = tutorial_app.Console(record=True)
    with patch.object(Path, "write_text", side_effect=OSError("boom")):
        tutorial_app.save_memory(core, file_path, console)
    assert "Failed to save memory" in console.export_text()
