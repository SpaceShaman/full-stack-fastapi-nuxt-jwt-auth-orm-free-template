from datetime import datetime, timedelta, timezone
from typing import Protocol
from uuid import uuid4

import jwt
from core.settings import SECRET_KEY
from mail.service import MailService
from users.repository import UserRepository
from users.schemas import User

from .exceptions import (
    ActivationCodeNotFound,
    IncorrectUsernameOrPassword,
    PasswordIsTooWeak,
    UserAlreadyExists,
    UserIsNotActive,
)
from .password_utils import (
    check_password_strength,
    generate_password_hash,
    verify_password,
)
from .schemas import ChangePasswordSchema, Token


class LoginRepositoryInterface(Protocol):
    def get_user_with_password(self, username: str) -> User | None: ...


class RegisterRepositoryInterface(Protocol):
    def create_user(
        self, username: str, password: str, email: str, activation_code: str
    ) -> None: ...
    def get_user_by_activation_code(self, activation_code: str) -> User | None: ...
    def update_user(self, user: User) -> None: ...


class ChangePasswordRepositoryInterface(Protocol):
    def get_user_with_password(self, username: str) -> User | None: ...
    def update_user(self, user: User) -> None: ...


class MailServiceInterface(Protocol):
    def send_activation_code(self, email: str, activation_code: str) -> None: ...


class LoginService:
    def __init__(self) -> None:
        self.user_repository: LoginRepositoryInterface = UserRepository()

    def login(self, username: str, password: str) -> Token:
        user = self.user_repository.get_user_with_password(username)
        if not user or not verify_password(password, user.password):
            raise IncorrectUsernameOrPassword("Incorrect username or password")
        if not user.is_active:
            raise UserIsNotActive("User is not active")
        return Token(
            access_token=self._create_access_token(username), token_type="bearer"
        )

    def _create_access_token(self, username: str) -> str:
        return jwt.encode(
            {"sub": username, "exp": self._get_expire()},
            SECRET_KEY,
            algorithm="HS256",
        )

    def _get_expire(self) -> datetime:
        return datetime.now(timezone.utc) + timedelta(days=7)


class RegisterService:
    def __init__(self) -> None:
        self.user_repository: RegisterRepositoryInterface = UserRepository()
        self.mail_service: MailServiceInterface = MailService()

    def register(self, username: str, password: str, email: str) -> None:
        if not check_password_strength(password):
            raise PasswordIsTooWeak("Password is too weak")
        hashed_password = generate_password_hash(password)
        activation_code = self._generate_activation_code()
        try:
            self.user_repository.create_user(
                username, hashed_password, email, activation_code
            )
            self.mail_service.send_activation_code(email, activation_code)
        except Exception as e:
            raise UserAlreadyExists("User already exists") from e

    def activate(self, activation_code: str) -> None:
        user = self.user_repository.get_user_by_activation_code(activation_code)
        if not user:
            raise ActivationCodeNotFound("Activation code not found")
        user.is_active = True
        user.activation_code = None
        self.user_repository.update_user(user)

    def _generate_activation_code(self) -> str:
        return str(uuid4())


class ChangePasswordService:
    def __init__(self) -> None:
        self.user_repository: ChangePasswordRepositoryInterface = UserRepository()

    def change_password(self, username: str, passwords: ChangePasswordSchema) -> None:
        user = self.user_repository.get_user_with_password(username)
        if not user or not verify_password(passwords.old_password, user.password):
            raise IncorrectUsernameOrPassword("Incorrect username or password")
        if not check_password_strength(passwords.new_password):
            raise PasswordIsTooWeak("Password is too weak")
        user.password = generate_password_hash(passwords.new_password)
        self.user_repository.update_user(user)
