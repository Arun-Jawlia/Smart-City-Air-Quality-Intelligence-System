"""
Application Configuration

Loads all project settings from environment variables.
"""

from pathlib import Path
import os

from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Project Root
BASE_DIR = Path(__file__).resolve().parent.parent

# -----------------------
# API Configuration
# -----------------------

WEATHER_BASE_URL = os.getenv("WEATHER_BASE_URL")

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

AQI_API_KEY = os.getenv("AQI_API_KEY")

# -----------------------
# Database
# -----------------------

DATABASE_NAME = os.getenv("DATABASE_NAME", "air_quality.db")

# -----------------------
# Paths
# -----------------------

RAW_DATA_PATH = BASE_DIR / os.getenv(
    "RAW_DATA_PATH",
    "data/raw",
)

PROCESSED_DATA_PATH = BASE_DIR / os.getenv(
    "PROCESSED_DATA_PATH",
    "data/processed",
)

MODEL_PATH = BASE_DIR / os.getenv(
    "MODEL_PATH",
    "models/aqi_model.pkl",
)

# -----------------------
# Logging
# -----------------------

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")