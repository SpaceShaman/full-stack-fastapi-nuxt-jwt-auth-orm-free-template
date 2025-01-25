from fastapi import FastAPI

app = FastAPI()


@app.get("/products")
async def get_products():
    return []
