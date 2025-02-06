import jwt
from core.settings import SECRET_KEY
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

from .exceptions import UserNotFound
from .schemas import User
from .services import UserService

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    try:
        return UserService().get_user(_decode_token(token).get("sub"))
    except UserNotFound as exc:
        raise HTTPException(status_code=401, detail="User not found") from exc


def _decode_token(token: str) -> dict:
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except jwt.ExpiredSignatureError as e:
        raise HTTPException(status_code=401, detail="Token has expired") from e
    except jwt.InvalidTokenError as e:
        raise HTTPException(status_code=401, detail="Invalid token") from e
