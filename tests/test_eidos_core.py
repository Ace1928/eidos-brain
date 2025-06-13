import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.eidos_core import EidosCore


def test_memory_and_reflection():
    core = EidosCore()
    core.remember("hello")
    assert core.reflect() == ["hello"]


def test_recurse_adds_insights():
    core = EidosCore()
    core.remember("hello")
    core.recurse()
    memories = core.reflect()
    assert any(isinstance(m, dict) for m in memories)
    assert len(memories) == 2


def test_process_cycle_combines_steps():
    core = EidosCore()
    core.process_cycle("data")
    memories = core.reflect()
    assert "data" in memories
    assert any(isinstance(m, dict) and m.get("repr") == "'data'" for m in memories)
    assert len(memories) == 2


def test_save_and_load_memory_methods(tmp_path):
    core = EidosCore()
    core.remember("hello")
    path = tmp_path / "mem.txt"
    core.save_memory(path)

    new_core = EidosCore()
    new_core.load_memory(path)
    assert new_core.reflect() == ["hello"]


def test_process_cycle_with_persistence(tmp_path):
    path = tmp_path / "cycle.txt"
    core = EidosCore()
    core.process_cycle("data", memory_path=path)
    assert path.exists()
    lines = path.read_text().splitlines()
    assert "data" in lines
    assert len(lines) == 2
