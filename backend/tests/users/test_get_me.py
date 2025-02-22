import jwt
import pytest

URL = "/users/me"


def _create_user(connection, username: str):
    connection.execute(
        f"INSERT INTO users (username, password, email) VALUES ('{username}', 'xxx', 'test@test.com')"
    )
    connection.commit()


@pytest.fixture(autouse=True)
def setup_db(db_connection):
    _create_user(
        db_connection,
        "user",
    )


def test_get_me(client, db_connection):
    jwt_token = jwt.encode({"sub": "user"}, "test", algorithm="HS256")

    response = client.get(URL, headers={"Authorization": f"Bearer {jwt_token}"})

    assert response.status_code == 200
    response = response.json()
    assert response["username"] == "user"


def test_get_me_invalid_token(client):
    response = client.get(URL, headers={"Authorization": "Bearer invalid_token"})

    assert response.status_code == 401


def test_get_me_expired_token(client):
    jwt_token = jwt.encode({"sub": "user", "exp": 0}, "test", algorithm="HS256")

    response = client.get(URL, headers={"Authorization": f"Bearer {jwt_token}"})

    assert response.status_code == 401


def test_get_me_user_not_found(client):
    jwt_token = jwt.encode({"sub": "not_found"}, "test", algorithm="HS256")

    response = client.get(URL, headers={"Authorization": f"Bearer {jwt_token}"})

    assert response.status_code == 401
