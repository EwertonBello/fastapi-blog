from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import get_settings


# SQLALCHEMY_DATABASE_URL = get_settings().database_url
# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

# SQLALCHEMY_DATABASE_URL = f'mysql+pymysql://root:@localhost/{get_settings().mysql_database}'   

_user = get_settings().mysql_username
_password = get_settings().mysql_root_password
_host = get_settings().mysql_host
_database_name = get_settings().mysql_database

SQLALCHEMY_DATABASE_URL = f"mysql://{_user}:{_password}@{_host}/{_database_name}?charset=utf8"
# SQLALCHEMY_DATABASE_URL = f"mysql://root:password@{_host}/sample_db"
# SQLALCHEMY_DATABASE_URL = "mysql://root:secret@127.0.0.1/blog_db"


engine = create_engine(SQLALCHEMY_DATABASE_URL, encoding="utf-8")

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()

# with engine.connect() as con:

#     rs = con.execute('SELECT * FROM new_table')

#     for row in rs:
#         print(row)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()