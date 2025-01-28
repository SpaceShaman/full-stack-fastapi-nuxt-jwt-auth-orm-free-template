from database.connection import db_connect

from .models import UserWithPassword


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
