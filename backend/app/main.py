from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlift import up
from users.api import router


@asynccontextmanager
async def migrate(app):
    yield up(migrations_path="database/migrations")


app = FastAPI(lifespan=migrate, root_path="/api")

app.include_router(router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
