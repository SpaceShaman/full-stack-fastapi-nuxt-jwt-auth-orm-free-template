from typing import Protocol

from .exceptions import UserNotFound
from .repository import UserRepository
from .schemas import User


class UserRepositoryInterface(Protocol):
    def get_user_by_username(self, username) -> User | None: ...
    def get_users(self) -> list[User]: ...


class UserService:
    def __init__(self) -> None:
        self.repository: UserRepositoryInterface = UserRepository()

    def get_user(self, username) -> User:
        if user := self.repository.get_user_by_username(username):
            return user
        else:
            raise UserNotFound(f"User {username} not found")

    def get_users(self) -> list[User]:
        return self.repository.get_users()
