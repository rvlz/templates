from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from .config import get_settings

Base = declarative_base()


def create_session(database_url):
    engine = create_engine(database_url)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return SessionLocal()


def get_db(settings = Depends(get_settings)):
    db = create_session(settings.DATABASE_URL)
    try:
        yield db
    finally:
        db.close()
