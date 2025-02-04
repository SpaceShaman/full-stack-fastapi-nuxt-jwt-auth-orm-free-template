from uuid import UUID

from passlib.context import CryptContext


def _create_user(
    connection,
    username: str,
    hashed_password: str,
    is_active: bool = False,
    activation_code: str = "94121a26-91c5-4303-b456-654818926474",
):
    connection.execute(
        f"INSERT INTO users (username, password, is_active, activation_code) VALUES ('{username}', '{hashed_password}', {is_active}, '{activation_code}')"
    )
    connection.commit()


def assert_user(connection, username: str, password: str, is_active: bool):
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    user = connection.execute(
        f"SELECT username, password, is_active, activation_code FROM users WHERE username = '{username}'"
    ).fetchone()
    assert user[0] == username
    assert pwd_context.verify(password, user[1])
    assert user[2] == is_active
    assert UUID(user[3])


def test_register_new_user(client, db_connection):
    response = client.post(
        "/auth/register", data={"username": "new-user", "password": "password"}
    )

    assert response.status_code == 200
    assert_user(
        db_connection,
        "new-user",
        "password",
        False,
    )


def test_try_register_existing_user(client, db_connection):
    _create_user(
        db_connection,
        "new-user",
        "xxxx",
    )

    response = client.post(
        "/auth/register", data={"username": "new-user", "password": "password"}
    )

    assert response.status_code == 403


def test_activate_registered_user(client, db_connection):
    _create_user(
        db_connection,
        "new-user",
        "$2b$12$AIflVbmr.Re2WQ1EhvB2Yu2WRPFklJAjMfQ8LGPiCYDUrcXtxslqe",
        False,
        "94121a26-91c5-4303-b456-654818926474",
    )

    response = client.get("/auth/activate/94121a26-91c5-4303-b456-654818926474")

    assert response.status_code == 200
    assert_user(
        db_connection,
        "new-user",
        "password",
        True,
    )
