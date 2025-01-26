from contextlib import asynccontextmanager

from fastapi import FastAPI
from products.api import router as products_router
from sqlift import up


@asynccontextmanager
async def migrate(app: FastAPI):
    up()
    yield


app = FastAPI(lifespan=migrate)


app.include_router(products_router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
