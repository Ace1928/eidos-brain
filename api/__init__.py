"""Expose the FastAPI application factory and default app instance."""

from .app import create_app, app

__all__ = ["create_app", "app"]
