import re
from uuid import UUID

from passlib.context import CryptContext

from tests.utils import create_user

URL = "/users/auth/register"


def assert_user(
    connection,
    username: str,
    password: str,
    is_active: bool,
    email: str,
):
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    user = connection.execute(
        f"SELECT username, password, is_active, email, activation_code FROM users WHERE username = '{username}'"
    ).fetchone()
    assert user[0] == username
    assert pwd_context.verify(password, user[1])
    assert user[2] == is_active
    assert user[3] == email
    if is_active:
        assert user[4] is None
    else:
        assert UUID(user[4])


def get_activation_code(message: str) -> str:
    if activation_code := re.search('/activate/(.*)"', message):
        return activation_code[1]
    return ""


def assert_mail(mail_spy, recipient: str):
    activation_code = get_activation_code(mail_spy.message)
    assert mail_spy.recipients[0] == recipient
    assert "Subject: Activate your account" in mail_spy.message
    assert UUID(activation_code)


def test_register_new_user(client, db_connection, mail_spy):
    response = client.post(
        URL,
        json={
            "username": "new-user",
            "password": "Passw0rd$",
            "email": "test@test.com",
        },
    )

    assert response.status_code == 200
    assert_user(
        db_connection,
        "new-user",
        "Passw0rd$",
        False,
        "test@test.com",
    )
    assert_mail(mail_spy, "test@test.com")


def test_try_register_existing_user(client, db_connection):
    create_user(
        db_connection,
        "new-user",
        "xxxx",
    )

    response = client.post(
        URL,
        json={
            "username": "new-user",
            "password": "Passw0rd$",
            "email": "test@test.com",
        },
    )

    assert response.status_code == 403


def test_try_register_user_with_existing_email(client, db_connection):
    create_user(
        db_connection,
        "new-user",
        "xxxx",
        email="test@test.com",
    )

    response = client.post(
        URL,
        json={
            "username": "another-user",
            "password": "Passw0rd$",
            "email": "test@test.com",
        },
    )

    assert response.status_code == 403


def test_try_register_user_with_weak_password(client, db_connection):
    response = client.post(
        URL,
        json={"username": "new-user", "password": "password", "email": "test@test.com"},
    )

    assert response.status_code == 401


def test_try_register_user_with_short_password(client, db_connection):
    response = client.post(
        URL,
        json={"username": "new-user", "password": "Pass0D$", "email": "test@test.com"},
    )

    assert response.status_code == 401


def test_try_register_user_with_no_number_in_password(client, db_connection):
    response = client.post(
        URL,
        json={
            "username": "new-user",
            "password": "Password$",
            "email": "test@test.com",
        },
    )

    assert response.status_code == 401


def test_try_register_user_with_no_uppercase_in_password(client, db_connection):
    response = client.post(
        URL,
        json={
            "username": "new-user",
            "password": "passw0rd$",
            "email": "test@test.com",
        },
    )

    assert response.status_code == 401


def test_try_register_user_with_no_special_char_in_password(client, db_connection):
    response = client.post(
        URL,
        json={"username": "new-user", "password": "Passw0rd", "email": "test@test.com"},
    )

    assert response.status_code == 401


def test_activate_registered_user(client, db_connection):
    create_user(
        db_connection,
        "new-user",
        "$2b$12$AIflVbmr.Re2WQ1EhvB2Yu2WRPFklJAjMfQ8LGPiCYDUrcXtxslqe",
        False,
        "94121a26-91c5-4303-b456-654818926474",
    )

    response = client.get("/users/auth/activate/94121a26-91c5-4303-b456-654818926474")

    assert response.status_code == 200
    assert_user(db_connection, "new-user", "password", True, "test@test.com")


def test_try_activate_not_existing_user(client, db_connection):
    response = client.get("/users/auth/activate/94121a26-91c5-4303-b456-654818926474")

    assert response.status_code == 404
