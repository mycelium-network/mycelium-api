from tests import utils


def test_read_root():
    response = utils.CLIENT.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "status": "running",
        "swagger_ui": "/docs",
        "redoc": "/redoc",
        "openid_connect": "/.well-known/openid-configuration"
    }
