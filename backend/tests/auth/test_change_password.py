import pytest
from passlib.context import CryptContext

URL = "/auth/change-password"


def create_user(
    connection,
    username: str,
    hashed_password: str,
    is_active: bool = True,
):
    connection.execute(
        f"INSERT INTO users (username, password, is_active, email) VALUES ('{username}', '{hashed_password}', {is_active}, 'test@test.com')"
    )
    connection.commit()


@pytest.fixture(autouse=True)
def setup_db(db_connection):
    create_user(
        db_connection,
        "user",
        "$2b$12$AIflVbmr.Re2WQ1EhvB2Yu2WRPFklJAjMfQ8LGPiCYDUrcXtxslqe",
    )


def assert_user(
    connection,
    username: str,
    password: str,
):
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    user = connection.execute(
        f"SELECT username, password FROM users WHERE username = '{username}'"
    ).fetchone()
    assert user[0] == username
    assert pwd_context.verify(password, user[1])


def test_change_password(logged_client, db_connection):
    response = logged_client.post(
        URL,
        json={"old_password": "password", "new_password": "new_password"},
    )

    assert response.status_code == 200
    assert_user(db_connection, "user", "new_password")
