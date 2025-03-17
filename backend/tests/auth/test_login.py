from datetime import datetime, timedelta, timezone

import jwt
import pytest

URL = "/users/auth/login"


def _create_user(
    connection,
    username: str,
    hashed_password: str,
    is_active: bool = True,
    email: str = "test@test.com",
):
    connection.execute(
        f"INSERT INTO users (username, password, is_active, email) VALUES ('{username}', '{hashed_password}', {is_active}, '{email}')"
    )
    connection.commit()


@pytest.fixture(autouse=True)
def setup_db(db_connection):
    _create_user(
        db_connection,
        "user",
        "$2b$12$AIflVbmr.Re2WQ1EhvB2Yu2WRPFklJAjMfQ8LGPiCYDUrcXtxslqe",
    )


def test_login_and_get_jwt(client, db_connection):
    response = client.post(URL, json={"username": "user", "password": "password"})

    assert response.status_code == 200
    response = response.json()
    assert "access_token" in response
    assert "token_type" in response
    assert response["token_type"] == "bearer"
    decoded = jwt.decode(response["access_token"], "test", algorithms=["HS256"])
    assert decoded["sub"] == "user"
    predicted_exp = int((datetime.now(timezone.utc) + timedelta(days=7)).timestamp())
    assert decoded["exp"] == predicted_exp


def test_login_with_wrong_password(client, db_connection):
    response = client.post(URL, json={"username": "user", "password": "wrong-password"})

    assert response.status_code == 401
    assert response.json() == {"detail": "Incorrect username or password"}


def test_login_with_wrong_username(client, db_connection):
    response = client.post(
        URL, json={"username": "wrong-username", "password": "password"}
    )

    assert response.status_code == 401
    assert response.json() == {"detail": "Incorrect username or password"}


def test_login_with_not_active_user(client, db_connection):
    _create_user(
        db_connection,
        "not-active-user",
        "$2b$12$AIflVbmr.Re2WQ1EhvB2Yu2WRPFklJAjMfQ8LGPiCYDUrcXtxslqe",
        False,
        "not-active@test.com",
    )

    response = client.post(
        URL, json={"username": "not-active-user", "password": "password"}
    )

    assert response.status_code == 403
    assert response.json() == {"detail": "User is not active"}
