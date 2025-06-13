import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.config import load_config


def test_load_config_defaults(monkeypatch):
    monkeypatch.delenv("EIDOS_VECTOR_MEMORY", raising=False)
    monkeypatch.delenv("EIDOS_API_KEY", raising=False)
    cfg = load_config()
    assert cfg.vector_memory is False
    assert cfg.api_key is None


def test_load_config_env(monkeypatch):
    monkeypatch.setenv("EIDOS_VECTOR_MEMORY", "true")
    monkeypatch.setenv("EIDOS_API_KEY", "secret")
    cfg = load_config()
    assert cfg.vector_memory is True
    assert cfg.api_key == "secret"
