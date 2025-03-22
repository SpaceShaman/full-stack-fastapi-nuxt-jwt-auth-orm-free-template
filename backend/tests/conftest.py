import os
from pathlib import Path
from sqlite3 import Connection
from typing import Any, Generator

import jwt
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
def logged_client(client: TestClient) -> TestClient:
    jwt_token = jwt.encode({"sub": "user"}, "test", algorithm="HS256")
    client.headers.update({"Authorization": f"Bearer {jwt_token}"})
    return client


@pytest.fixture
def mail_spy(mocker) -> Any:
    class SMTPSpy:
        def __init__(self):
            self.from_address = None
            self.recipients = None
            self.message = None

        def login(self, user, password):
            pass

        def sendmail(self, from_addr, to_addrs, msg):
            self.from_address = from_addr
            self.recipients = to_addrs
            self.message = msg

    mail = SMTPSpy()

    class ContextManager:
        def __init__(self, *args, **kwargs):
            pass

        def __enter__(self):
            return mail

        def __exit__(self, *args):
            pass

    mocker.patch("mail.client.SMTP_SSL", return_value=ContextManager())
    yield mail
