import os
from pathlib import Path
from sqlite3 import Connection
from typing import Any, Generator

import pytest
from fastapi.testclient import TestClient

MIGRATION_PATH = str(Path(__file__).parent.parent / "app" / "database" / "migrations")


@pytest.fixture(autouse=True)
def setup_env():
    os.environ["DB_URL"] = "sqlite:///file::memory:?cache=shared"
    os.environ["SECRET_KEY"] = "test"


@pytest.fixture
def db_connection() -> Generator[Connection, Any, None]:
    from database.connection import db_connect
    from sqlift import down, up

    with db_connect() as connection:
        up(migrations_path=MIGRATION_PATH)
        yield connection
        down(migrations_path=MIGRATION_PATH)


@pytest.fixture
def client() -> TestClient:
    from main import app

    return TestClient(app)


@pytest.fixture
def mail_spy(mocker) -> Any:
    class MailClientSpy:
        def __init__(self):
            self.recipient = None
            self.subject = None
            self.body = None

        def send_mail(self, recipients: list[str], subject: str, body: str) -> None:
            self.recipients = recipients
            self.subject = subject
            self.body = body

    mail = MailClientSpy()
    mocker.patch("mail.services.MailClient", return_value=mail)
    yield mail
