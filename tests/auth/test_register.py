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
        f"INSERT INTO users (username, password, is_active, activation_code, email) VALUES ('{username}', '{hashed_password}', {is_active}, '{activation_code}', 'test@test.com')"
    )
    connection.commit()


def assert_user(connection, username: str, password: str, is_active: bool, email: str):
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    user = connection.execute(
        f"SELECT username, password, is_active, email, activation_code FROM users WHERE username = '{username}'"
    ).fetchone()
    assert user[0] == username
    assert pwd_context.verify(password, user[1])
    assert user[2] == is_active
    assert user[3] == email
    assert UUID(user[4])


def assert_mail(mail_spy, recipient: str):
    activation_code = mail_spy.body.split(": ")[1]
    assert mail_spy.recipients[0] == recipient
    assert mail_spy.subject == "Activate your account"
    assert UUID(activation_code)


def test_register_new_user(client, db_connection, mail_spy):
    response = client.post(
        "/auth/register",
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
    _create_user(
        db_connection,
        "new-user",
        "xxxx",
    )

    response = client.post(
        "/auth/register",
        json={
            "username": "new-user",
            "password": "Passw0rd$",
            "email": "test@test.com",
        },
    )

    assert response.status_code == 403


def test_try_register_user_with_weak_password(client, db_connection):
    response = client.post(
        "/auth/register",
        json={"username": "new-user", "password": "password", "email": "test@test.com"},
    )

    assert response.status_code == 401


def test_try_register_user_with_short_password(client, db_connection):
    response = client.post(
        "/auth/register",
        json={"username": "new-user", "password": "Pass0D$", "email": "test@test.com"},
    )

    assert response.status_code == 401


def test_try_register_user_with_no_number_in_password(client, db_connection):
    response = client.post(
        "/auth/register",
        json={
            "username": "new-user",
            "password": "Password$",
            "email": "test@test.com",
        },
    )

    assert response.status_code == 401


def test_try_register_user_with_no_uppercase_in_password(client, db_connection):
    response = client.post(
        "/auth/register",
        json={
            "username": "new-user",
            "password": "passw0rd$",
            "email": "test@test.com",
        },
    )

    assert response.status_code == 401


def test_try_register_user_with_no_special_char_in_password(client, db_connection):
    response = client.post(
        "/auth/register",
        json={"username": "new-user", "password": "Passw0rd", "email": "test@test.com"},
    )

    assert response.status_code == 401


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
    assert_user(db_connection, "new-user", "password", True, "test@test.com")
