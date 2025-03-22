import pytest

URL = "/users"


def _create_user(connection, username: str, email: str, is_active: bool):
    connection.execute(
        f"INSERT INTO users (username, password, email, is_active) VALUES ('{username}', 'xxx', '{email}', {is_active})"
    )
    connection.commit()


@pytest.fixture(autouse=True)
def setup_db(db_connection):
    _create_user(
        db_connection,
        "user",
        "user@test.com",
        True,
    )
    _create_user(
        db_connection,
        "user_1",
        "user_1@test.com",
        False,
    )
    _create_user(
        db_connection,
        "user_2",
        "user_2@test.com",
        True,
    )


def test_get_users_list(logged_client):
    response = logged_client.get(URL)

    assert response.status_code == 200
    assert len(response.json()) == 3
    assert response.json() == [
        {
            "username": "user",
            "is_active": True,
            "email": "user@test.com",
        },
        {
            "username": "user_1",
            "is_active": False,
            "email": "user_1@test.com",
        },
        {
            "username": "user_2",
            "is_active": True,
            "email": "user_2@test.com",
        },
    ]


def test_try_get_users_list_without_auth(client):
    response = client.get(URL)

    assert response.status_code == 401
    assert response.json() == {"detail": "Not authenticated"}
