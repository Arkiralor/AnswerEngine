from pydantic import ConfigDict
from os import environ, path
from pathlib import Path

class Settings(ConfigDict):
    BASE_PATH = Path(__file__).resolve().parent.parent
    SECRET_KEY: str = environ("SECRET_KEY", "$up3r-$3cr34-|<3V")

    MONGO_HOST: str = environ("MONGO_HOST", "localhost")
    MONGO_NAME: str = environ("MONGO_NAME", "mongo-database")
    MONGO_USER: str = environ("MONGO_USER", "user")
    MONGO_PASSWORD: str = environ("MONGO_PASSWORD", "password")
    MONGO_PORT: str = environ("MONGO_PORT", "8000")
    MONGO_URI: str = environ("MONGO_URI", "")

    MAX_ITEMS_PER_PAGE: int = 10

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()