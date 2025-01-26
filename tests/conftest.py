import os
from sqlite3 import Connection
from typing import Any, Generator

import pytest
from database import db_connect
from sqlift import down, up


@pytest.fixture
def connection() -> Generator[Connection, Any, None]:
    os.environ["DB_URL"] = "sqlite:///file::memory:?cache=shared"
    with db_connect() as connection:
        up(migrations_path="app/migrations")
        yield connection
        down(migrations_path="app/migrations")
