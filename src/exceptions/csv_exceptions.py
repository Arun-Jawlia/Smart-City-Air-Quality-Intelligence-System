"""
Custom exceptions used by CSV Loader.
"""


class CSVLoaderError(Exception):
    """Base exception for CSV Loader."""


class CSVFileNotFoundError(CSVLoaderError):
    """Raised when CSV file is missing."""


class CSVEmptyError(CSVLoaderError):
    """Raised when dataset is empty."""


class CSVSchemaError(CSVLoaderError):
    """Raised when required columns are missing."""


class CSVParsingError(CSVLoaderError):
    """Raised when pandas cannot parse the CSV."""