from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache
from typing import Set


class Settings(BaseSettings):
    TASK_API_ENDPOIN: str

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


@lru_cache()
def get_settings():
    return Settings()


settings = get_settings()
