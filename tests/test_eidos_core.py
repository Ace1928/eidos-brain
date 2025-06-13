import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.eidos_core import EidosCore
from core.event_bus import EventBus
from core.eidos_core import (
    EVENT_EXPERIENCE_STORED,
    EVENT_RECURSE_COMPLETED,
)


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


def test_event_bus_emits_actions():
    events: list[str] = []
    bus = EventBus()
    bus.subscribe(EVENT_EXPERIENCE_STORED, lambda *_: events.append("stored"))
    bus.subscribe(EVENT_RECURSE_COMPLETED, lambda *_: events.append("recurse"))

    core = EidosCore(event_bus=bus)
    core.process_cycle("info")

    assert "stored" in events
    assert "recurse" in events
