import os
from pathlib import Path
from pydantic import BaseSettings

BASE_DIR = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    DEBUG: bool = False
    ARCHIVE_PASSWORD: str = "Pass"
    TEMP_DATA_PATH: str = os.path.join(BASE_DIR, "temp_data")
    INPUT_PATH: str = os.path.join(BASE_DIR, "input")

    class Config:
        env_file = os.path.join(BASE_DIR, '.env')


settings = Settings()
