"""FastAPI service exposing EidosCore operations."""

from __future__ import annotations

import os

from fastapi import FastAPI

from core.eidos_core import EidosCore

HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", "8000"))
ENABLE_UI = os.getenv("ENABLE_UI", "false").lower() == "true"

app = FastAPI(title="Eidos API", docs_url="/docs" if ENABLE_UI else None)
core = EidosCore()


@app.get("/memories")
def get_memories() -> list[object]:
    """Return stored memories."""
    return core.reflect()


@app.post("/remember")
def add_memory(experience: str) -> dict[str, str]:
    """Store a new experience."""
    core.remember(experience)
    return {"status": "stored"}


@app.post("/recurse")
def run_recurse() -> dict[str, str]:
    """Run recursion on current memories."""
    core.recurse()
    return {"status": "recurred"}


@app.post("/process")
def process(experience: str) -> dict[str, str]:
    """Remember an experience and immediately recurse."""
    core.process_cycle(experience)
    return {"status": "processed"}


def main() -> None:
    """Launch the API server."""
    import uvicorn

    uvicorn.run("api.server:app", host=HOST, port=PORT, reload=False)


if __name__ == "__main__":
    main()
