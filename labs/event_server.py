"""WebSocket server streaming :mod:`core.event_bus` messages."""

from __future__ import annotations

import asyncio


import websockets
from websockets.server import WebSocketServer, WebSocketServerProtocol

from core.event_bus import EventBus


async def handle_client(bus: EventBus, websocket: WebSocketServerProtocol) -> None:
    """Forward published messages from ``bus`` to ``websocket``."""
    queue = bus.subscribe()
    try:
        while True:
            message = await queue.get()
            await websocket.send(message)
    except websockets.ConnectionClosed:
        pass
    finally:
        bus.unsubscribe(queue)


async def start_server(
    bus: EventBus, host: str = "localhost", port: int = 8765
) -> WebSocketServer:
    """Return a running WebSocket server bound to ``host`` and ``port``."""

    async def _handler(websocket: WebSocketServerProtocol) -> None:
        await handle_client(bus, websocket)

    return await websockets.serve(_handler, host, port)


async def main() -> None:
    """Run a server using a local :class:`EventBus`."""
    bus = EventBus()

    server = await start_server(bus)
    try:
        while True:
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        server.close()
        await server.wait_closed()


if __name__ == "__main__":
    asyncio.run(main())
