from fastapi import FastAPI
from products.api import router as products_router

app = FastAPI()


app.include_router(products_router)
