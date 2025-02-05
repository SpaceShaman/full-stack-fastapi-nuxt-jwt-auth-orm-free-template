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


@pytest.fixture
def mail_spy(mocker) -> Any:
    class MailServiceSpy:
        def __init__(self):
            self.activation_code = None
            self.email = None

        def send_activation_code(self, email: str, activation_code: str) -> None:
            self.email = email
            self.activation_code = activation_code

    mail = MailServiceSpy()
    mocker.patch("auth.services.MailService", return_value=mail)
    yield mail
