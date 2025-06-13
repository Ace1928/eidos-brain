"""Publish messages to subscribed consumers."""

from __future__ import annotations

import asyncio
from typing import List


class EventBus:
    """Simple publish/subscribe message bus."""

    def __init__(self) -> None:
        self._queues: List[asyncio.Queue[str]] = []

    def subscribe(self) -> asyncio.Queue[str]:
        """Return a queue that receives published messages."""
        queue: asyncio.Queue[str] = asyncio.Queue()
        self._queues.append(queue)
        return queue

    def unsubscribe(self, queue: asyncio.Queue[str]) -> None:
        """Remove ``queue`` from subscribers."""
        try:
            self._queues.remove(queue)
        except ValueError:
            pass

    def publish(self, message: str) -> None:
        """Send ``message`` to all subscribers."""
        for queue in list(self._queues):
            queue.put_nowait(message)
