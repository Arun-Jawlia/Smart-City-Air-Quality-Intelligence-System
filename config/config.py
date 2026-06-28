from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

AQI_API_KEY = os.getenv("AQI_API_KEY")

DATABASE_NAME = os.getenv("DATABASE_NAME")

RAW_DATA_PATH = BASE_DIR / os.getenv("RAW_DATA_PATH")

PROCESSED_DATA_PATH = BASE_DIR / os.getenv("PROCESSED_DATA_PATH")

MODEL_PATH = BASE_DIR / os.getenv("MODEL_PATH")

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")