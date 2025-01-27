from auth.api import auth_router
from database.migration import migrate
from fastapi import FastAPI
from products.api import products_router

app = FastAPI(lifespan=migrate)

app.include_router(products_router)
app.include_router(auth_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
