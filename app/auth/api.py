from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from .exceptions import (
    IncorrectUsernameOrPassword,
    PasswordIsTooWeak,
    UserAlreadyExists,
    UserIsNotActive,
)
from .models import Token
from .services import LoginService, RegisterService

auth_router = APIRouter(prefix="/auth", tags=["auth"])


@auth_router.post("/login")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]) -> Token:
    try:
        return LoginService().login(form_data.username, form_data.password)
    except IncorrectUsernameOrPassword as e:
        raise HTTPException(
            status_code=401, detail="Incorrect username or password"
        ) from e
    except UserIsNotActive as e:
        raise HTTPException(status_code=401, detail="User is not active") from e


@auth_router.post("/register")
async def register(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> dict[str, str]:
    try:
        RegisterService().register(form_data.username, form_data.password)
    except UserAlreadyExists as e:
        raise HTTPException(status_code=403, detail="User already exists") from e
    except PasswordIsTooWeak as e:
        raise HTTPException(status_code=401, detail="Password is too weak") from e
    return {"register": "success"}


@auth_router.get("/activate/{activation_code}")
async def activate(activation_code: str) -> dict[str, str]:
    RegisterService().activate(activation_code)
    return {"activation": "success"}
