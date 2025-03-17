import re
from uuid import UUID

from passlib.context import CryptContext

from tests.utils import create_user

URL = "users/auth/recover"


def assert_user(
    connection, username: str, password: str, is_active: bool, recovery_code: str
):
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    user = connection.execute(
        f"SELECT username, password, is_active, activation_code FROM users WHERE username = '{username}'"
    ).fetchone()
    assert user[0] == username
    assert pwd_context.verify(password, user[1])
    assert user[2] == is_active
    assert user[3] == recovery_code
    if recovery_code:
        assert UUID(recovery_code)


def get_recover_code(mail_body: str) -> str:
    if recover_code := re.search('/recover/(.*)"', mail_body):
        return recover_code[1]
    return ""


def assert_mail(mail_spy, recipient: str):
    recover_code = get_recover_code(mail_spy.body)
    assert mail_spy.recipients[0] == recipient
    assert mail_spy.subject == "Recover your password"
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
    recover_code = get_recover_code(mail_spy.body)
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
