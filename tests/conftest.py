import os

import pytest
from database import db_connect
from sqlift import down, up


@pytest.fixture
def connection():
    os.environ["DB_URL"] = "sqlite:///file::memory:?cache=shared"
    with db_connect() as connection:
        up()
        yield connection
        down()
