from auth.router import auth_router
from core.settings import BASE_URL
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from users.router import users_router

app = FastAPI(root_path="/api")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[f"http://{BASE_URL}", f"https://{BASE_URL}"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users_router)
app.include_router(auth_router)
