from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Autonomous AI Agent API"
    app_version: str = "0.1.0"
    debug: bool = True


@lru_cache()
def get_settings() -> Settings:
    return Settings()
