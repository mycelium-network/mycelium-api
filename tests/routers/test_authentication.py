from tests import utils


def test_authenticate_johndoe():
    response = utils.authentication_user("johndoe", "secret")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"

    access_token = response.json()["access_token"]
    token_type = response.json()["token_type"]

    assert token_type == "bearer"
    assert utils.verify_bearer_token(access_token)


def test_authenticate_alice():
    response = utils.authentication_user("alice", "secret")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"

    access_token = response.json()["access_token"]
    token_type = response.json()["token_type"]

    assert token_type == "bearer"
    assert utils.verify_bearer_token(access_token)


def test_authenticate_bob():
    response = utils.authentication_user("bob", "secret")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"

    access_token = response.json()["access_token"]
    token_type = response.json()["token_type"]

    assert token_type == "bearer"
    assert utils.verify_bearer_token(access_token)


def test_authenticate_invalid_username():
    response = utils.authentication_user("foobar", "secret")
    assert response.status_code == 401
    assert response.headers["content-type"] == "application/json"
    assert response.json() == {
        "detail": "Incorrect username or password"
    }


def test_authenticate_invalid_password():
    response = utils.authentication_user("johndoe", "notthepassword")
    assert response.status_code == 401
    assert response.headers["content-type"] == "application/json"
    assert response.json() == {
        "detail": "Incorrect username or password"
    }
