import os

import pytest
from database import db_connect
from sqlift import up


@pytest.fixture
def connection():
    os.environ["DB_URL"] = "sqlite:///test.sqlite"
    with db_connect() as connection:
        up()
        yield connection
    os.remove("test.sqlite")
