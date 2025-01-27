from contextlib import asynccontextmanager

from auth.api import auth_router
from fastapi import FastAPI
from products.api import products_router
from sqlift import up


@asynccontextmanager
async def migrate(app: FastAPI):
    up()
    yield


app = FastAPI(lifespan=migrate)

app.include_router(products_router)
app.include_router(auth_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
