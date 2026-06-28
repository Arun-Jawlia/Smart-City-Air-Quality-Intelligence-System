from config import config

def main():
    print("Smart City Air Quality Intelligence System")
    print("Project Root :", config.BASE_DIR)
    print("Database :", config.DATABASE_NAME)
    print("Raw Path :", config.RAW_DATA_PATH)
    print("Log Level :", config.LOG_LEVEL)


if __name__ == "__main__":
    main()