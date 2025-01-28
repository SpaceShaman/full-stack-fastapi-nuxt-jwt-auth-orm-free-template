from typing import Protocol

from users.models import UserWithPassword
from users.repositorys import UserRepository

from .exceptions import IncorrectUsernameOrPassword
from .models import Token
from .utils import verify_password


class UserRepositoryInterface(Protocol):
    def get_user_with_password(self, username: str) -> UserWithPassword | None: ...


class AuthService:
    def __init__(self) -> None:
        self.user_repository: UserRepositoryInterface = UserRepository()

    def login(self, username: str, password: str) -> Token:
        user = self.user_repository.get_user_with_password(username)
        if not user or not verify_password(password, user.password):
            raise IncorrectUsernameOrPassword("Incorrect username or password")
        return Token(access_token="token", token_type="bearer")
