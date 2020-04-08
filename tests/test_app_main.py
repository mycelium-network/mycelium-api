from fastapi.testclient import TestClient
import jwt
from jwt import PyJWTError

import app.config as config
from app.main import app

CLIENT = TestClient(app)


def test_read_root():
    response = CLIENT.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "status": "running",
        "swagger_ui": "/docs",
        "redoc": "/redoc",
        "openid_connect": "/.well-known/openid-configuration"
    }


def authentication_user(username: str, password: str):
    response = CLIENT.post(
        "/token",
        data={"grant_type": "", "username": username, "password": password,
              "scope": "", "client_id": "", "client_secret": ""}
    )
    return response


def verify_bearer_token(token: str):
    try:
        payload = jwt.decode(token, config.PUBLIC_KEY,
                             algorithms=[config.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            return False
    except PyJWTError:
        return False
    return True


def test_authenticate_johndoe():
    response = authentication_user("johndoe", "secret")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"

    access_token = response.json()["access_token"]
    token_type = response.json()["token_type"]

    assert token_type == "bearer"
    assert verify_bearer_token(access_token)


def test_authenticate_alice():
    response = authentication_user("alice", "secret")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"

    access_token = response.json()["access_token"]
    token_type = response.json()["token_type"]

    assert token_type == "bearer"
    assert verify_bearer_token(access_token)


def test_authenticate_bob():
    response = authentication_user("bob", "secret")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"

    access_token = response.json()["access_token"]
    token_type = response.json()["token_type"]

    assert token_type == "bearer"
    assert verify_bearer_token(access_token)


def test_authenticate_invalid_user():
    response = authentication_user("foobar", "foobar")
    assert response.status_code == 401
    assert response.headers["content-type"] == "application/json"
    assert response.json() == {
        "detail": ""
    }
