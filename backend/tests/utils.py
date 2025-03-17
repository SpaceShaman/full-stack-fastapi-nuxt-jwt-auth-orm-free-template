from sqlite3 import Connection


def create_user(
    connection: Connection,
    username: str,
    hashed_password: str,
    is_active: bool = False,
    activation_code: str | None = "94121a26-91c5-4303-b456-654818926474",
    email: str = "test@test.com",
):
    connection.execute(
        f"INSERT INTO users (username, password, is_active, activation_code, email) VALUES ('{username}', '{hashed_password}', {is_active}, '{activation_code}', '{email}')"
    )
    connection.commit()
