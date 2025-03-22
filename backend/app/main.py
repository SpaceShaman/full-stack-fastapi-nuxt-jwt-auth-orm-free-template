from auth.router import auth_router
from fastapi import FastAPI
from users.router import users_router

app = FastAPI(root_path="/api")

app.include_router(users_router)
app.include_router(auth_router)
