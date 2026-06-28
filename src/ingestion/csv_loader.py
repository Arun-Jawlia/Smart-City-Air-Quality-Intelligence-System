"""
csv_loader.py

Production-ready CSV Loader
"""

from pathlib import Path
import pandas as pd
from src.utils.logger import get_logger
logger = get_logger(__name__)

Path("data/raw/dataset.csv")

class CSVLoader:
    #  Loading CSV File safely
    def __init__(self, file_path : str):
        self.file_path = Path(file_path)

    
    def file_exists(self) -> bool:
        if not self.file_path.exists():
            logger.error(f"CSV file not found: {self.file_path}")
            raise FileNotFoundError(
                f"CSV file not found: {self.file_path}"
            )

        return True
        
    def load(self) -> pd.DataFrame:

        self.file_exists()

        logger.info(f"Loading CSV: {self.file_path}")

        df = pd.read_csv(self.file_path)

        if df.empty:
            logger.error("Dataset is empty")
            raise ValueError("Dataset is empty")
        
        logger.info(
            f"Dataset loaded successfully. Rows={df.shape[0]}, Columns={df.shape[1]}"
        )
        return df