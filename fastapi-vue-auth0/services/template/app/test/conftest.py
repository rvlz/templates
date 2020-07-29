import os

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.main import create_app
from app.main.database import Base
from app.main.api.user.models import User


@pytest.fixture
def engine():
    _engine = create_engine(os.getenv("DATABASE_TEST_URL"))
    tables = [User.__table__]
    Base.metadata.create_all(bind=_engine, tables=tables)
    yield _engine
    Base.metadata.drop_all(bind=_engine, tables=tables)


@pytest.fixture
def session(engine):
    Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    _session = Session()
    yield _session
    _session.close()


@pytest.fixture
def client():
    _client = TestClient(create_app())
    yield _client
