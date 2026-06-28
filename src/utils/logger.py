"""
Logger Utility

Provides a reusable logger for every module.
"""

import logging

# Ensure logging configuration is loaded
from configs import logging_config  # noqa: F401


def get_logger(name: str) -> logging.Logger:
    """
    Return a configured logger.

    Args:
        name: Module name.

    Returns:
        Configured logger instance.
    """
    return logging.getLogger(name)