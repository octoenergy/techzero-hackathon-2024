from os import getenv as e

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

db_host = e("POSTGRES_HOST")
db_name = e("POSTGRES_DB")
db_password = e("POSTGRES_PASSWORD")
db_port = e("POSTGRES_PORT")
db_user = e("POSTGRES_USER")

db_dsn = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

engine = create_engine(
    db_dsn,
    echo=True,
)

CustomSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = CustomSession()
    try:
        yield db
    finally:
        db.close()
