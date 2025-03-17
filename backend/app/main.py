from fastapi import FastAPI
from users.router import router

app = FastAPI(root_path="/api")

app.include_router(router)
