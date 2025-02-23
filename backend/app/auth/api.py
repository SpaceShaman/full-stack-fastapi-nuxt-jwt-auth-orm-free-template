from fastapi import APIRouter, HTTPException, Request

from .exceptions import (
    IncorrectUsernameOrPassword,
    PasswordIsTooWeak,
    UserAlreadyExists,
    UserIsNotActive,
)
from .schemas import Credentials, RegistrationSchema, Token
from .services import LoginService, RegisterService

auth_router = APIRouter(prefix="/auth", tags=["auth"])


@auth_router.post("/login")
async def login(credentials: Credentials) -> Token:
    try:
        return LoginService().login(credentials.username, credentials.password)
    except IncorrectUsernameOrPassword as e:
        raise HTTPException(
            status_code=401, detail="Incorrect username or password"
        ) from e
    except UserIsNotActive as e:
        raise HTTPException(status_code=403, detail="User is not active") from e


@auth_router.post("/register")
async def register(request: Request, user: RegistrationSchema) -> dict[str, str]:
    try:
        RegisterService().register(
            user.username,
            user.password,
            user.email,
        )
    except UserAlreadyExists as e:
        raise HTTPException(status_code=403, detail="User already exists") from e
    except PasswordIsTooWeak as e:
        raise HTTPException(status_code=401, detail="Password is too weak") from e
    return {"register": "success"}


@auth_router.get("/activate/{activation_code}")
async def activate(activation_code: str) -> dict[str, str]:
    try:
        RegisterService().activate(activation_code)
    except Exception as e:
        raise HTTPException(status_code=404, detail="Activation code not found") from e
    return {"activation": "success"}
