from pydantic_settings import BaseSettings
from pydantic import AnyHttpUrl
from typing import List


class Settings(BaseSettings):
    app_name: str = "Minha API"
    env: str = "dev"
    database_url: str
    cors_origins: List[AnyHttpUrl] | List[str] = []

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
