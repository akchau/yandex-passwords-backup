import os
from pathlib import Path
from pydantic import BaseSettings

BASE_DIR = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    # Режим работы
    DEBUG: bool
    ARCHIVE_PASSWORD: str
    TEMP_DATA_PATH: str = os.path.join(BASE_DIR, "temp_data")
    INPUT_PATH: str

    class Config:
        env_file = os.path.join(BASE_DIR, '.env')


settings = Settings()