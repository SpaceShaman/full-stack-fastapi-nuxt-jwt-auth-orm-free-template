from typing import Annotated

from fastapi import APIRouter, Depends

from .auth.api import auth_router
from .dependencies import get_current_user
from .schemas import User

router = APIRouter(prefix="/users")
router.include_router(auth_router)
users_router = APIRouter(tags=["users"])


@users_router.get("/me", response_model_exclude_none=True)
async def get_me(user: Annotated[User, Depends(get_current_user)]) -> User:
    return user


router.include_router(users_router)
