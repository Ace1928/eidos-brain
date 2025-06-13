from fastapi.testclient import TestClient
from api.app import create_app


def test_add_and_get_memory() -> None:
    client = TestClient(create_app())
    add = client.post("/memory", json={"experience": "hello"})
    assert add.status_code == 200
    get = client.get("/memory")
    assert get.status_code == 200
    assert "hello" in get.json()


def test_agent_endpoints() -> None:
    client = TestClient(create_app())
    util = client.post("/agent/utility", json={"task": "clean"})
    assert util.json()["result"] == "Performed clean"
    exp = client.post("/agent/experiment", json={"hypothesis": "h1"})
    assert exp.json()["result"] == "Experimenting with h1"


def test_openapi_docs_available() -> None:
    client = TestClient(create_app())
    resp = client.get("/openapi.json")
    assert resp.status_code == 200
    assert resp.json()["info"]["title"] == "Eidos API"
