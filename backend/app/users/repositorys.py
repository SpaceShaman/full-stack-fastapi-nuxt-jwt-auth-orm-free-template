from database.connection import db_connect

from .schemas import User


class UserRepository:
    def get_user_with_password(self, username: str) -> User | None:
        with db_connect() as connection:
            cursor = connection.execute(
                "SELECT username, password, is_active FROM users WHERE username = ?",
                (username,),
            )
            user = cursor.fetchone()
            return (
                User(username=user[0], password=user[1], is_active=user[2])
                if user
                else None
            )

    def get_user(self, username: str) -> User | None:
        with db_connect() as connection:
            cursor = connection.execute(
                "SELECT username, is_active FROM users WHERE username = ?", (username,)
            )
            user = cursor.fetchone()
            return User(username=user[0], is_active=user[1]) if user else None

    def get_user_by_activation_code(self, activation_code: str) -> User | None:
        with db_connect() as connection:
            cursor = connection.execute(
                "SELECT username, is_active FROM users WHERE activation_code = ?",
                (activation_code,),
            )
            user = cursor.fetchone()
            return User(username=user[0], is_active=user[1]) if user else None

    def create_user(
        self, username: str, password: str, email: str, activation_code: str
    ) -> None:
        with db_connect() as connection:
            connection.execute(
                "INSERT INTO users (username, password, email, activation_code) VALUES (?, ?, ?, ?)",
                (username, password, email, activation_code),
            )
            connection.commit()

    def update_user(self, user: User) -> None:
        with db_connect() as connection:
            connection.execute(
                "UPDATE users SET is_active = ?, activation_code = ? WHERE username = ?",
                (user.is_active, user.activation_code, user.username),
            )
            connection.commit()
