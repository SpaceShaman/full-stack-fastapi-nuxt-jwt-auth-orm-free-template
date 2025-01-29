from typing import Annotated

from fastapi import APIRouter, Depends

from .dependencies import get_current_user
from .models import User

users_router = APIRouter(prefix="/users", tags=["users"])


@users_router.get("/me")
async def get_me(user: Annotated[User, Depends(get_current_user)]) -> User:
    return user
