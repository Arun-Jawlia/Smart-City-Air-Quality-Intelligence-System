from configs import config
from src.ingestion.csv_loader import CSVLoader


def main():
    print("Smart City Air Quality Intelligence System")
    print("Project Root :", config.BASE_DIR)
    print("Database :", config.DATABASE_NAME)
    print("Raw Path :", config.RAW_DATA_PATH)
    print("Log Level :", config.LOG_LEVEL)

    loader = CSVLoader(
        file_path="data/external/historical_aqi.csv",
        required_columns=[
            "Date",
            "AQI",
            "Temperature",
            "Humidity",
        ],
    )

    df = loader.load()

    print(df.head())


if __name__ == "__main__":
    main()