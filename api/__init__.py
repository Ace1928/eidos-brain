"""API package exposing EidosCore through FastAPI."""
"""Minimal WSGI API exposing Eidos services."""

from .server import create_app, run_server

__all__ = ["create_app", "run_server"]
