from database.connection import db_connect

from .models import User, UserWithPassword


class UserRepository:
    def get_user_with_password(self, username: str) -> UserWithPassword | None:
        with db_connect() as connection:
            cursor = connection.execute(
                "SELECT username, password FROM users WHERE username = ?", (username,)
            )
            user = cursor.fetchone()
            return (
                UserWithPassword(username=user[0], password=user[1]) if user else None
            )

    def get_user(self, username: str) -> User | None:
        with db_connect() as connection:
            cursor = connection.execute(
                "SELECT username, is_active FROM users WHERE username = ?", (username,)
            )
            user = cursor.fetchone()
            return User(username=user[0], is_active=user[1]) if user else None

    def create_user(self, username: str, password: str, activation_code: str) -> None:
        with db_connect() as connection:
            connection.execute(
                "INSERT INTO users (username, password, activation_code) VALUES (?, ?, ?)",
                (username, password, activation_code),
            )
            connection.commit()

    def activate_user(self, activation_code: str) -> None:
        with db_connect() as connection:
            connection.execute(
                "UPDATE users SET is_active = 1 WHERE activation_code = ?",
                (activation_code,),
            )
            connection.commit()
