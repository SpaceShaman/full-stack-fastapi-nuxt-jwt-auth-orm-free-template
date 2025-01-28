import pytest


def _create_user(connection, username: str, hashed_password: str):
    connection.execute(
        f"INSERT INTO users (username, password) VALUES ('{username}', '{hashed_password}')"
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
    response = client.post(
        "/auth/login", data={"username": "user", "password": "password"}
    )

    assert response.status_code == 200
    response = response.json()
    assert "access_token" in response
    assert "token_type" in response
    assert response["token_type"] == "bearer"


def test_login_with_wrong_password(client, db_connection):
    response = client.post(
        "/auth/login", data={"username": "user", "password": "wrong-password"}
    )

    assert response.status_code == 400
    assert response.json() == {"detail": "Incorrect username or password"}


def test_login_with_wrong_username(client, db_connection):
    response = client.post(
        "/auth/login", data={"username": "wrong-username", "password": "password"}
    )

    assert response.status_code == 400
    assert response.json() == {"detail": "Incorrect username or password"}
