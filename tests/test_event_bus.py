import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.event_bus import EventBus


def test_publish_subscribe() -> None:
    bus = EventBus()
    q1 = bus.subscribe()
    q2 = bus.subscribe()
    bus.publish("hello")
    assert q1.get_nowait() == "hello"
    assert q2.get_nowait() == "hello"
