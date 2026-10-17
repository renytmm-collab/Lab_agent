from pydantic_settings import BaseSettings,SettingsConfigDict
from pathlib import Path

BASE_DIR=Path(__file__).resolve().parent.parent

class Settings(BaseSettings):
    DATABASE_URL: str
    JWT_SECRET_KEY: str
    JWT_EXPIRE_HOURS: int
    JWT_ALGORITHM: str
    model_config=SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8"
    )

settings=Settings()