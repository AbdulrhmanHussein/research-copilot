from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

ROOT_DIR = Path(__file__).resolve().parent.parent.parent.parent


class Settings(BaseSettings):

    APP_NAME: str
    APP_VERSION: str

    model_config = SettingsConfigDict(
        env_file=str(ROOT_DIR / ".env"), env_file_encoding="utf-8", extra="ignore"
    )


def get_settings():
    return Settings()
