import os
from datetime import datetime, timedelta, timezone
from typing import Protocol
from uuid import uuid4

import jwt
from passlib.context import CryptContext
from users.models import UserWithPassword
from users.repositorys import UserRepository

from .exceptions import IncorrectUsernameOrPassword
from .models import Token


class LoginRepositoryInterface(Protocol):
    def get_user_with_password(self, username: str) -> UserWithPassword | None: ...


class RegisterRepositoryInterface(Protocol):
    def create_user(
        self, username: str, password: str, activation_code: str
    ) -> None: ...


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class LoginService:
    def __init__(self) -> None:
        self.user_repository: LoginRepositoryInterface = UserRepository()

    def login(self, username: str, password: str) -> Token:
        user = self.user_repository.get_user_with_password(username)
        if not user or not self._verify_password(password, user.password):
            raise IncorrectUsernameOrPassword("Incorrect username or password")
        return Token(access_token=_create_access_token(username), token_type="bearer")

    def _verify_password(self, plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)


class RegisterService:
    def __init__(self) -> None:
        self.user_repository: RegisterRepositoryInterface = UserRepository()

    def register(self, username: str, password: str) -> Token:
        hashed_password = self._generate_password_hash(password)
        self.user_repository.create_user(
            username, hashed_password, self._generate_activation_code()
        )
        return Token(access_token=_create_access_token(username), token_type="bearer")

    def _generate_password_hash(self, password: str) -> str:
        return pwd_context.hash(password)

    def _generate_activation_code(self) -> str:
        return str(uuid4())


def _create_access_token(username: str) -> str:
    return jwt.encode(
        {"sub": username, "exp": _get_expire()},
        os.getenv("SECRET_KEY"),
        algorithm="HS256",
    )


def _get_expire() -> datetime:
    return datetime.now(timezone.utc) + timedelta(days=7)
