"""Logging helpers for structured output."""

import logging
from typing import Literal

_LOG_FORMAT = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"


def configure_logging(level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = "INFO") -> None:
    """Configure root logger with a single stdio handler."""

    logging.basicConfig(level=level, format=_LOG_FORMAT)
