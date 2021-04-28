from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import get_settings

_user = get_settings().postgres_user
_password = get_settings().postgres_password
_host = get_settings().postgres_host
_database_name = get_settings().postgres_db

SQLALCHEMY_DATABASE_URL = f"postgresql://{_user}:{_password}@{_host}/{_database_name}"


engine = create_engine(SQLALCHEMY_DATABASE_URL, encoding="utf-8")

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()