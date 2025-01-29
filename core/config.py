#config.py
import os
from functools import lru_cache
from typing import Optional

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    PROJECT_NAME: str = "Swift task manager 🔥"
    PROJECT_VERSION: str = "0.1.0"
    DEBUG: bool = False
    API_V1_STR: str = "/api/v1"
    JWT_SECRET: str = "your-secret-key"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15
    TEST_DATABASE_URL: Optional[str] = None

    # Database Settings
    POSTGRES_USER: str = os.getenv("POSTGRES_USER", "postgres")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", "")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "localhost")
    POSTGRES_PORT: str = str(os.getenv("POSTGRES_PORT", "5432"))
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "swift_task_mgr_db")

    class Config:
        case_sensitive = True
        env_file = ".env"  # Load from a .env file if available

    @property
    def database_url(self) -> str:
        return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
