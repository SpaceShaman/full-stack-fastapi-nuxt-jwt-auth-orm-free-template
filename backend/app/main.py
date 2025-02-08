from contextlib import asynccontextmanager

from auth.api import auth_router
from fastapi import FastAPI
from sqlift import up
from users.api import users_router


@asynccontextmanager
async def migrate(app):
    yield up(migrations_path="database/migrations")


app = FastAPI(lifespan=migrate, root_path="/api")

app.include_router(auth_router)
app.include_router(users_router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
