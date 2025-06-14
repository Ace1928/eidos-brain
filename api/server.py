"""WSGI server exposing health-check endpoints."""

from __future__ import annotations

from typing import Callable, Iterable
from wsgiref.simple_server import make_server

from core.health import HealthChecker


def create_app(checker: HealthChecker | None = None) -> Callable:
    """Return a WSGI app providing ``/healthz``."""

    checker = checker or HealthChecker()

    def app(environ: dict, start_response: Callable) -> Iterable[bytes]:
        path = environ.get("PATH_INFO", "")
        if environ.get("REQUEST_METHOD") == "GET" and path == "/healthz":
            status = "200 OK"
            body = checker.check()
            start_response(status, [("Content-Type", "application/json")])
            return [f"{{\"status\": \"{body['status']}\"}}".encode()]

        start_response("404 Not Found", [("Content-Type", "text/plain")])
        return [b"Not Found"]

    return app


def run_server(host: str = "0.0.0.0", port: int = 8000) -> None:
    """Launch the WSGI server."""

    with make_server(host, port, create_app()) as httpd:
        httpd.serve_forever()


if __name__ == "__main__":
    run_server()
