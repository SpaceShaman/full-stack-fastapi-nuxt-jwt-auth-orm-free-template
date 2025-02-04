from uuid import UUID

from passlib.context import CryptContext

URL = "/auth/register"


def assert_user(connection, username: str, password: str, is_active: bool):
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    user = connection.execute(
        f"SELECT username, password, is_active, activation_code FROM users WHERE username = '{username}'"
    ).fetchone()
    assert user[0] == username
    assert pwd_context.verify(password, user[1])
    assert user[2] == is_active
    assert UUID(user[3])


def test_register(client, db_connection):
    response = client.post(URL, data={"username": "new-user", "password": "password"})

    assert response.status_code == 200
    response = response.json()
    assert "access_token" in response
    assert "token_type" in response
    assert response["token_type"] == "bearer"

    assert_user(
        db_connection,
        "new-user",
        "password",
        False,
    )
