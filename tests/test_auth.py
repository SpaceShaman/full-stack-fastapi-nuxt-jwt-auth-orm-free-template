def test_login_and_get_jwt(client, db_connection):
    response = client.post(
        "/auth/login", data={"username": "user1", "password": "password1"}
    )

    assert response.status_code == 200
    response = response.json()
    assert "access_token" in response
    assert "token_type" in response
    assert response["token_type"] == "bearer"
