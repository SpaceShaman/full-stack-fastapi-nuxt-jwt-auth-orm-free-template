import os
from datetime import datetime, timedelta, timezone
from typing import Protocol

import jwt
from passlib.context import CryptContext
from users.models import UserWithPassword
from users.repositorys import UserRepository

from .exceptions import IncorrectUsernameOrPassword
from .models import Token


class UserRepositoryInterface(Protocol):
    def get_user_with_password(self, username: str) -> UserWithPassword | None: ...
    def create_user(self, username: str, password: str) -> None: ...


class AuthService:
    def __init__(self) -> None:
        self.user_repository: UserRepositoryInterface = UserRepository()
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def login(self, username: str, password: str) -> Token:
        user = self.user_repository.get_user_with_password(username)
        if not user or not self._verify_password(password, user.password):
            raise IncorrectUsernameOrPassword("Incorrect username or password")
        return Token(
            access_token=self._create_access_token(username), token_type="bearer"
        )

    def register(self, username: str, password: str) -> Token:
        hashed_password = self._generate_password_hash(password)
        self.user_repository.create_user(username, hashed_password)
        return Token(
            access_token=self._create_access_token(username), token_type="bearer"
        )

    def _generate_password_hash(self, password: str) -> str:
        return self.pwd_context.hash(password)

    def _verify_password(self, plain_password, hashed_password):
        return self.pwd_context.verify(plain_password, hashed_password)

    def _create_access_token(self, username: str) -> str:
        return jwt.encode(
            {"sub": username, "exp": self._get_expire()},
            os.getenv("SECRET_KEY"),
            algorithm="HS256",
        )

    def _get_expire(self) -> datetime:
        return datetime.now(timezone.utc) + timedelta(days=7)
