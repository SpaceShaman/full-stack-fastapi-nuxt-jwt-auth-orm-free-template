from contextlib import contextmanager
from sqlite3 import Connection, connect
from typing import Generator


@contextmanager
def db_connect(
    database: str = "db.sqlite",
) -> Generator[Connection, None, None]:
    connection = connect(database)
    connection.execute("PRAGMA foreign_keys = ON")
    connection.execute("PRAGMA journal_mode = WAL")
    try:
        yield connection
    finally:
        connection.close()
