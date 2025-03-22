from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Request

from users.dependencies import get_current_user
from users.schemas import User

from .exceptions import (
    ActivationCodeNotFound,
    IncorrectUsernameOrPassword,
    PasswordIsTooWeak,
    UserAlreadyExists,
    UserIsNotActive,
    UserNotFound,
)
from .schemas import (
    ChangePasswordSchema,
    Credentials,
    RecoverPasswordSchema,
    RegistrationSchema,
    SetNewPasswordSchema,
    Token,
)
from .services import (
    ChangePasswordService,
    LoginService,
    RecoverPasswordService,
    RegisterService,
)

auth_router = APIRouter(tags=["auth"], prefix="/auth")


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
    except ActivationCodeNotFound as e:
        raise HTTPException(status_code=404, detail="Activation code not found") from e
    return {"activation": "success"}


@auth_router.post("/change-password")
async def change_password(
    user: Annotated[User, Depends(get_current_user)], passwords: ChangePasswordSchema
) -> dict[str, str]:
    try:
        ChangePasswordService().change_password(user.username, passwords)
    except IncorrectUsernameOrPassword as e:
        raise HTTPException(
            status_code=401, detail="Incorrect username or password"
        ) from e
    except PasswordIsTooWeak as e:
        raise HTTPException(status_code=401, detail="Password is too weak") from e
    return {"change-password": "success"}


@auth_router.post("/recover")
async def send_recovery_email(
    recover_password: RecoverPasswordSchema,
) -> dict[str, str]:
    try:
        RecoverPasswordService().send_recovery_email(recover_password.email)
    except UserNotFound as e:
        raise HTTPException(
            status_code=403, detail="User with this email does not exist"
        ) from e
    return {"detail": "Password reset email sent"}


@auth_router.post("/recover/{recovery_code}")
async def set_new_password(
    recovery_code: str,
    password: SetNewPasswordSchema,
) -> dict[str, str]:
    try:
        RecoverPasswordService().set_new_password(recovery_code, password.new_password)
    except ActivationCodeNotFound as e:
        raise HTTPException(status_code=403, detail="User not found") from e
    except PasswordIsTooWeak as e:
        raise HTTPException(status_code=401, detail="Password is too weak") from e
    return {"recover": "success"}
