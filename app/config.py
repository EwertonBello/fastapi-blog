from functools import lru_cache
from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Default Name"
    database_url: str = "sqlite:///./app/database.db"
    mysql_database: str = "my_db"
    mysql_host: str = "localhost"
    mysql_root_password: str
    mysql_username: str = "root"
    secret_key: str

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'

@lru_cache()
def get_settings():
    return Settings()
