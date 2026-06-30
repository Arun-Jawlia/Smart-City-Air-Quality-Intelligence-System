#pylint: disable = all
"""
csv_loader.py

Production-ready CSV Loader
"""

from pathlib import Path
import pandas as pd
from typing import List
from pandas.errors import EmptyDataError, ParserError

from src.exceptions.csv_exceptions import (
    CSVEmptyError,
    CSVFileNotFoundError,
    CSVParsingError,
    CSVSchemaError,
)

from src.utils.logger import get_logger
logger = get_logger(__name__)

Path("data/raw/dataset.csv")

class CSVLoader:
    #  Loading CSV File safely
    def __init__(self, file_path : str, required_columns: List[str], encoding: str = 'utf-8', delimiter: str = ','):
        self.file_path = Path(file_path)
        self.required_columns = required_columns
        self.encoding = encoding
        self.delimiter = delimiter

    
    def file_exists(self) -> bool:
        if not self.file_path.exists():
            logger.error(f"CSV file not found: {self.file_path}")
            raise FileNotFoundError(
                f"CSV file not found: {self.file_path}"
            )

        return True
        
    def load(self) -> pd.DataFrame:
        self._validate_file()

        logger.info(f"Loading {self.file_path.name}")

        try:
            df = pd.read_csv(
                self.file_path,
                encoding=self.encoding,
                delimiter=self.delimiter,
            )

        except EmptyDataError as exc:
            logger.error("Dataset is empty.")

            raise CSVEmptyError(
                "Dataset contains no records."
            ) from exc

        except ParserError as exc:
            logger.error("CSV parsing failed.")

            raise CSVParsingError(
                "Invalid CSV format."
            ) from exc

        self._validate_dataframe(df)

        logger.info(
            f"Loaded {len(df)} rows and {len(df.columns)} columns."
        )

        return df

    def _validate_file(self) -> None:
        logger.info("Checking CSV file.")

        if not self.file_path.exists():
            logger.error(f"CSV file not found: {self.file_path}")

            raise CSVFileNotFoundError(
                f"{self.file_path} does not exist."
            )
        
    def _validate_dataframe(
        self,
        df: pd.DataFrame,
    ) -> None:

        if df.empty:
            raise CSVEmptyError("Dataset is empty.")

        missing_columns = [
            column
            for column in self.required_columns
            if column not in df.columns
        ]

        if missing_columns:
            raise CSVSchemaError(
                f"Missing columns: {missing_columns}"
            )