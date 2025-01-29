from contextlib import asynccontextmanager

from auth.api import auth_router
from fastapi import FastAPI
from products.api import products_router
from sqlift import up
from users.api import users_router


@asynccontextmanager
async def migrate(app):
    yield up()


app = FastAPI(lifespan=migrate)

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(products_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
