"""
Logging Configuration

Centralized logging setup for the project.
"""

import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

from configs import config

# Create logs directory
LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "project.log"

# Log format
LOG_FORMAT = (
    "%(asctime)s | "
    "%(levelname)s | "
    "%(name)s | "
    "%(message)s"
)

formatter = logging.Formatter(LOG_FORMAT)

# File Handler
file_handler = RotatingFileHandler(
    filename=LOG_FILE,
    maxBytes=5 * 1024 * 1024,
    backupCount=5,
)

file_handler.setFormatter(formatter)

# Console Handler
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

# Root Logger
logging.basicConfig(
    level=config.LOG_LEVEL,
    handlers=[
        file_handler,
        console_handler,
    ],
)