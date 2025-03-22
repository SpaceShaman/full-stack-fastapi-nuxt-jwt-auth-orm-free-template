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

    def get_user_by_username(self, username: str) -> User | None:
        return self._get_user("username = ?", (username,))

    def get_user_by_email(self, email: str) -> User | None:
        return self._get_user("email = ?", (email,))

    def get_user_by_activation_code(self, activation_code: str) -> User | None:
        return self._get_user(
            "activation_code = ?",
            (activation_code,),
        )

    def get_users(self) -> list[User]:
        with db_connect() as connection:
            cursor = connection.execute("SELECT username, email, is_active FROM users")
            users = cursor.fetchall()
            return [
                User(username=user[0], email=user[1], is_active=user[2])
                for user in users
            ]

    def _get_user(self, where: str, parms: tuple) -> User | None:
        with db_connect() as connection:
            cursor = connection.execute(
                f"SELECT username, is_active FROM users WHERE {where}",
                parms,
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
                self._build_update_query(user),
                self._get_update_parms(user),
            )
            connection.commit()

    def _build_update_query(self, user: User) -> str:
        query = "UPDATE users SET activation_code = ?, "
        if user.is_active is not None:
            query += "is_active = ?, "
        if user.password:
            query += "password = ?, "
        query = query[:-2]
        query += " WHERE username = ?"
        return query

    def _get_update_parms(self, user: User) -> tuple:
        parms: list[str | bool | None] = [user.activation_code]
        if user.is_active is not None:
            parms.append(user.is_active)
        if user.password:
            parms.append(user.password)
        parms.append(user.username)
        return tuple(parms)
