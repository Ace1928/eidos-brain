from __future__ import annotations

import logging
import os
import sys
from pathlib import Path

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.logging_config import configure_logging, DEFAULT_FORMAT


def test_configure_logging(tmp_path: Path) -> None:
    log_file = tmp_path / "out.log"
    logger = configure_logging(logging.DEBUG, log_file=str(log_file))

    logger.debug("message")

    content = log_file.read_text()
    assert "message" in content
    assert logger.level == logging.DEBUG
    assert any(isinstance(h, logging.FileHandler) for h in logger.handlers)
    assert any(isinstance(h, logging.StreamHandler) for h in logger.handlers)
    for handler in logger.handlers:
        assert handler.formatter._fmt == DEFAULT_FORMAT
