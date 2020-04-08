from tests import utils

ENDPOINT_PREFIX = "/auth"
USER_ME_ENDPOINT = ENDPOINT_PREFIX + "/users/me/"


def test_get_user_me_johndoe():
    response = utils.get_authorized_endpoint(USER_ME_ENDPOINT, "johndoe", "secret", utils.HEADER)
    assert response.status_code == 200
    assert response.json() == {
        "username": "johndoe",
        "email": "johndoe@example.com",
        "full_name": "John Doe",
        "disabled": False,
        "second_factor": False
    }


def test_get_user_me_alice():
    response = utils.get_authorized_endpoint(USER_ME_ENDPOINT, "alice", "secret", utils.HEADER)
    assert response.status_code == 400
    assert response.json() == {
        "detail": "Inactive user"
    }


def test_get_user_me_bob():
    response = utils.get_authorized_endpoint(USER_ME_ENDPOINT, "bob", "secret", utils.HEADER)
    assert response.status_code == 200
    assert response.json() == {
        "username": "bob",
        "email": "bob@example.com",
        "full_name": "Bob",
        "disabled": False,
        "second_factor": True
    }


def test_get_user_me_invalid_user():
    response = utils.get_authorized_endpoint(USER_ME_ENDPOINT, "foo", "bar", utils.HEADER)
    assert response.status_code == 401
    assert response.json() == {
        "detail": "Could not validate credentials"
    }
