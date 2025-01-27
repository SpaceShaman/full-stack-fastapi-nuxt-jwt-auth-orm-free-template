import os
from contextlib import contextmanager
from sqlite3 import Connection, connect
from typing import Generator


@contextmanager
def db_connect() -> Generator[Connection, None, None]:
    connection = connect(_get_database_path())
    connection.execute("PRAGMA foreign_keys = ON")
    connection.execute("PRAGMA journal_mode = WAL")
    try:
        yield connection
    finally:
        connection.close()


def _get_database_path() -> str:
    return os.environ.get("DB_URL", "sqlite:///db.sqlite").replace("sqlite:///", "")
