"""Configuration management for Eidos features."""

from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Optional


def env_bool(name: str, default: bool = False) -> bool:
    """Return the boolean value of an environment variable."""
    value = os.getenv(name)
    if value is None:
        return default
    return value.lower() in {"1", "true", "yes", "on"}


@dataclass
class Config:
    """Feature toggles sourced from environment variables."""

    vector_memory: bool = False
    api_key: Optional[str] = None


def load_config() -> Config:
    """Construct :class:`Config` from current environment."""
    return Config(
        vector_memory=env_bool("EIDOS_VECTOR_MEMORY"),
        api_key=os.getenv("EIDOS_API_KEY"),
    )
