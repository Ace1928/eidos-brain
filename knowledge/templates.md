# Templates

Use these snippets in conjunction with the strategies found in
`recursive_patterns.md`. Any terminology used below is defined in
`glossary_reference.md`.

## Function Template
```python
def function_name(param1: Type, param2: Type) -> ReturnType:
    """Brief description of the function."""
    # Logic goes here
    pass
```

## Class Template
```python
class ClassName:
    """One-line summary of class purpose."""

    def __init__(self, arg: Type) -> None:
        self.arg = arg
```

## CLI Application Template
```python
from rich.console import Console
from rich.prompt import Prompt

def main() -> None:
    """Entry point for interactive command-line tools."""
    console = Console()
    console.print("Welcome", style="bold")
    Prompt.ask("Press enter to continue")

if __name__ == "__main__":
    main()
```

## Test Template
```python
def test_feature() -> None:
    """Verify a specific behavior."""
    result = function_under_test()
    assert result == expected
```

## Async Function Template
```python
async def async_function(param: Type) -> ReturnType:
    """Brief description of the coroutine."""
    return await other_coroutine(param)
```

## Event Bus Template
```python
class EventBus:
    """Publish messages to subscribed queues."""

    def __init__(self) -> None:
        self.queues: list[asyncio.Queue[str]] = []

    def subscribe(self) -> asyncio.Queue[str]:
        queue: asyncio.Queue[str] = asyncio.Queue()
        self.queues.append(queue)
        return queue

    def publish(self, message: str) -> None:
        for q in self.queues:
            q.put_nowait(message)
```

## WebSocket Server Template
```python
async def start_server(bus: EventBus, host: str = "localhost", port: int = 8765) -> WebSocketServer:
    """Stream bus messages to WebSocket clients."""

    async def handler(ws: WebSocketServerProtocol) -> None:
        queue = bus.subscribe()
        try:
            while True:
                await ws.send(await queue.get())
        finally:
            bus.unsubscribe(queue)

    return await websockets.serve(handler, host, port)
```
