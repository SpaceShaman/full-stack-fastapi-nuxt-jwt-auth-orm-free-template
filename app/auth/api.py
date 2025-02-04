from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from .exceptions import IncorrectUsernameOrPassword, UserAlreadyExists
from .models import Token
from .services import LoginService, RegisterService

auth_router = APIRouter(prefix="/auth", tags=["auth"])


@auth_router.post("/login")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]) -> Token:
    try:
        return LoginService().login(form_data.username, form_data.password)
    except IncorrectUsernameOrPassword as e:
        raise HTTPException(
            status_code=400, detail="Incorrect username or password"
        ) from e


@auth_router.post("/register")
async def register(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]) -> Token:
    try:
        return RegisterService().register(form_data.username, form_data.password)
    except UserAlreadyExists as e:
        raise HTTPException(status_code=400, detail="User already exists") from e


@auth_router.get("/activate/{activation_code}")
async def activate(activation_code: str) -> dict[str, str]:
    RegisterService().activate(activation_code)
    return {"activation": "success"}
