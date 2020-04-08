from tests import utils

ENDPOINT_PREFIX = "/auth"
STATUS_ENDPOINT = ENDPOINT_PREFIX + "/2fa/status"

def test_status_unauthenticated():
    response = utils.CLIENT.get(STATUS_ENDPOINT)
    assert response.status_code == 401
    assert response.json() == {
        "detail": "Not authenticated"
    }


def test_status_johndoe():
    response = utils.get_authorized_endpoint(STATUS_ENDPOINT, "johndoe", "secret", utils.HEADER)
    assert response.status_code == 200
    assert response.json() == {
        "status": False
    }
    # response = utils.get_authorized_endpoint(STATUS_ENDPOINT, "johndoe", "secret", utils.COOKIE)
    # assert response.status_code == 200
    # assert response.json() == {
    #     "status": False
    # }

def test_status_alice():
    response = utils.get_authorized_endpoint(STATUS_ENDPOINT, "alice", "secret", utils.HEADER)
    assert response.status_code == 400
    assert response.json() == {
        "detail": "Inactive user"
    }
    # response = utils.get_authorized_endpoint(STATUS_ENDPOINT, "alice", "secret", utils.COOKIE)
    # assert response.status_code == 400
    # assert response.json() == {
    #     "detail": "Inactive user"
    # }

def test_status_bob():
    response = utils.get_authorized_endpoint(STATUS_ENDPOINT, "bob", "secret", utils.HEADER)
    assert response.status_code == 200
    assert response.json() == {
        "status": True
    }
    # response = utils.get_authorized_endpoint(STATUS_ENDPOINT, "bob", "secret", utils.COOKIE)
    # assert response.status_code == 200
    # assert response.json() == {
    #     "status": True
    # }
