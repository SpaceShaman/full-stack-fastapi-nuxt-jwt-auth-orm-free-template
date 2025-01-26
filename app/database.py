from contextlib import contextmanager
from sqlite3 import Connection, connect
from typing import Generator


@contextmanager
def db_connect() -> Generator[Connection, None, None]:
    connection = connect("db.sqlite")
    connection.execute("PRAGMA foreign_keys = ON")
    connection.execute("PRAGMA journal_mode = WAL")
    try:
        yield connection
    finally:
        connection.close()
