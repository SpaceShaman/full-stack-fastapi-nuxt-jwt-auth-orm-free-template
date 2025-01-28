import os
from sqlite3 import Connection
from typing import Any, Generator

import pytest
from fastapi.testclient import TestClient


@pytest.fixture(autouse=True)
def setup_env():
    os.environ["DB_URL"] = "sqlite:///file::memory:?cache=shared"
    os.environ["SECRET_KEY"] = "test"


@pytest.fixture
def db_connection() -> Generator[Connection, Any, None]:
    from database.connection import db_connect
    from sqlift import down, up

    with db_connect() as connection:
        up(migrations_path="app/migrations")
        yield connection
        down(migrations_path="app/migrations")


@pytest.fixture
def client() -> TestClient:
    from main import app

    return TestClient(app)
