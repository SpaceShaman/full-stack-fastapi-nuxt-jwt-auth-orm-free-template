from typing import Annotated

from fastapi import APIRouter, Depends

from .auth.router import auth_router
from .dependencies import get_current_user
from .schemas import User
from .service import UserService

users_router = APIRouter(prefix="/users")
users_router.include_router(auth_router)
router = APIRouter(tags=["users"])


@router.get("/", response_model_exclude_none=True)
async def get_users(user: Annotated[User, Depends(get_current_user)]) -> list[User]:
    return UserService().get_users()


@router.get("/me", response_model_exclude_none=True)
async def get_me(user: Annotated[User, Depends(get_current_user)]) -> User:
    return user


users_router.include_router(router)
