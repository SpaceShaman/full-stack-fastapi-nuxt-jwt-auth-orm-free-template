import re
from uuid import UUID

from passlib.context import CryptContext

from tests.utils import create_user

URL = "auth/recover"


def assert_user(
    connection, username: str, password: str, is_active: bool, recovery_code: str | None
):
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    user = connection.execute(
        f"SELECT username, password, is_active, activation_code FROM users WHERE username = '{username}'"
    ).fetchone()
    assert user[0] == username
    assert pwd_context.verify(password, user[1])
    assert user[2] == is_active
    assert user[3] == recovery_code


def get_recover_code(message: str) -> str:
    if recover_code := re.search('/recover/(.*)"', message):
        return recover_code[1]
    return ""


def assert_mail(mail_spy, recipient: str):
    recover_code = get_recover_code(mail_spy.message)
    assert mail_spy.recipients[0] == recipient
    assert "Subject: Recover your password" in mail_spy.message
    assert UUID(recover_code)


def test_send_recover_password(client, db_connection, mail_spy):
    create_user(
        db_connection,
        "user",
        "$2b$12$AIflVbmr.Re2WQ1EhvB2Yu2WRPFklJAjMfQ8LGPiCYDUrcXtxslqe",
        True,
        "",
    )

    response = client.post(
        URL,
        json={"email": "test@test.com"},
    )

    assert response.status_code == 200
    assert response.json() == {"detail": "Password reset email sent"}
    recover_code = get_recover_code(mail_spy.message)
    assert_user(db_connection, "user", "password", True, recover_code)
    assert_mail(mail_spy, "test@test.com")


def test_try_send_recover_password_for_not_existing_user(
    client, db_connection, mail_spy
):
    response = client.post(
        URL,
        json={"email": "not_existing_user@test.com"},
    )

    assert response.status_code == 403


def test_set_new_password_with_recover_code(client, db_connection):
    create_user(
        db_connection,
        "user",
        "$2b$12$AIflVbmr.Re2WQ1EhvB2Yu2WRPFklJAjMfQ8LGPiCYDUrcXtxslqe",
        True,
        "recover-code",
    )

    response = client.post(
        f"{URL}/recover-code",
        json={"new_password": "NewPassw0rd$"},
    )

    assert response.status_code == 200
    assert_user(
        db_connection,
        "user",
        "NewPassw0rd$",
        True,
        None,
    )


def test_try_set_new_password_with_wrong_recover_code(client, db_connection):
    response = client.post(
        f"{URL}/wrong-code",
        json={"new_password": "NewPassw0rd$"},
    )

    assert response.status_code == 403


def test_try_set_new_password_with_weak_password(client, db_connection):
    create_user(
        db_connection,
        "user",
        "$2b$12$AIflVbmr.Re2WQ1EhvB2Yu2WRPFklJAjMfQ8LGPiCYDUrcXtxslqe",
        True,
        "recover-code",
    )

    response = client.post(
        f"{URL}/recover-code",
        json={"new_password": "weak"},
    )

    assert response.status_code == 401
    assert_user(
        db_connection,
        "user",
        "password",
        True,
        "recover-code",
    )


def test_try_set_new_password_with_empty_recover_code(client, db_connection):
    response = client.post(
        f"{URL}/",
        json={"new_password": "NewPassw0rd$"},
    )
    assert response.status_code == 422
