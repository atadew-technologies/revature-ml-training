import os
from urllib.parse import quote_plus

from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{os.getenv('MYSQL_USER')}:{os.getenv('MYSQL_PASSWORD')}@{os.getenv('MYSQL_HOST')}/{os.getenv('MYSQL_DB')}"
print(SQLALCHEMY_DATABASE_URL)
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_size=20, max_overflow=0, echo_pool="debug",
)
SessionLocal = sessionmaker(autocommit=False, autoflush=True, expire_on_commit=False, bind=engine)

Base = declarative_base()


def get_session():
    try:
        yield SessionLocal
    except SQLAlchemyError as e:
        print(e)
