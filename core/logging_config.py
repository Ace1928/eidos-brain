"""Central logging configuration for the Eidos project."""

from __future__ import annotations

import logging
from logging import Logger

DEFAULT_FORMAT = "%(asctime)s [%(levelname)s] %(name)s: %(message)s"


def configure_logging(level: int = logging.INFO, log_file: str | None = None) -> Logger:
    """Configure and return the root logger.

    Parameters
    ----------
    level:
        Log level applied to the root logger.
    log_file:
        Optional file path to also receive log output.

    Returns
    -------
    Logger
        The configured root logger.
    """
    logger = logging.getLogger()
    logger.setLevel(level)

    formatter = logging.Formatter(DEFAULT_FORMAT)

    for handler in list(logger.handlers):
        logger.removeHandler(handler)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger
