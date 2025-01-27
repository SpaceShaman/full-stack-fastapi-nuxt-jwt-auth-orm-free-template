from contextlib import asynccontextmanager

from sqlift import up


@asynccontextmanager
async def migrate(app):
    up()
    yield
