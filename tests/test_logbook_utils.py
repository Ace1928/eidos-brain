from datetime import datetime, timezone
from pathlib import Path
from tools import logbook_entry


def test_read_logbook_missing(tmp_path: Path) -> None:
    path = tmp_path / "none.md"
    text = logbook_entry.read_logbook(path)
    assert text == "# Eidos Logbook\n"


def test_next_cycle_number_gaps() -> None:
    text = "# Eidos Logbook\n\n## Cycle 1:\n- a\n\n## Cycle 3:\n- c\n"
    assert logbook_entry.next_cycle_number(text) == 4


def test_format_entry_without_next(monkeypatch) -> None:
    fixed_time = datetime(2024, 1, 1, 0, 0, tzinfo=timezone.utc)

    class FixedDatetime(datetime):
        @classmethod
        def now(cls, tz=None):
            return fixed_time

    monkeypatch.setattr(logbook_entry, "datetime", FixedDatetime)
    entry = logbook_entry.format_entry(5, "info")
    assert "## Cycle 5: 2024-01-01 00:00 UTC" in entry
    assert entry.endswith("\n")


def test_append_entry_creates_file(tmp_path: Path, monkeypatch) -> None:
    fixed_time = datetime(2024, 1, 1, 12, 0, tzinfo=timezone.utc)

    class FixedDatetime(datetime):
        @classmethod
        def now(cls, tz=None):
            return fixed_time

    monkeypatch.setattr(logbook_entry, "datetime", FixedDatetime)
    path = tmp_path / "log.md"
    logbook_entry.append_entry("first", None, path)
    assert path.exists()
    content = path.read_text()
    assert "## Cycle 1:" in content
    assert "- first" in content
