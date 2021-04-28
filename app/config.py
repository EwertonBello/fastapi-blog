from functools import lru_cache
from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Default Name"
    database_url: str = "sqlite:///./app/database.db"
    postgres_db: str = "my_db"
    postgres_host: str = "localhost"
    postgres_password: str
    postgres_user: str = "root"
    secret_key: str

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'

@lru_cache()
def get_settings():
    return Settings()
