from typing import Protocol

from .exceptions import UserNotFound
from .repositorys import UserRepository
from .schemas import User


class UserRepositoryInterface(Protocol):
    def get_user(self, username) -> User | None: ...


class UserService:
    def __init__(self) -> None:
        self.repository: UserRepositoryInterface = UserRepository()

    def get_user(self, username) -> User:
        if user := self.repository.get_user(username):
            return user
        else:
            raise UserNotFound(f"User {username} not found")
