from fastapi.testclient import TestClient
import jwt
from jwt import PyJWTError

import app.config as config
from app.main import app

CLIENT = TestClient(app)

COOKIE = 1
HEADER = 2


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


def get_authorized_endpoint(endpoint, username, password, cookie_or_header):
    if cookie_or_header == HEADER:
        auth_response = authentication_user(username, password)
        if auth_response.status_code != 200:
            response = CLIENT.get(
                endpoint,
                headers={
                    "Authorization": "Bearer "+"N/A"
                }
            )
            return response
        access_token = auth_response.json()["access_token"]
        response = CLIENT.get(
            endpoint,
            headers={
                "Authorization": "Bearer "+access_token
            }
        )
        return response
    if cookie_or_header == COOKIE:
        auth_response = authentication_user(username, password)
        if auth_response.status_code != 200:
            response = CLIENT.get(
                endpoint,
                cookies={
                    "session": "N/A"
                }
            )
            return response
        access_token = auth_response.json()["access_token"]
        response = CLIENT.get(
            endpoint,
            cookies={
                "session": access_token
            }
        )
        return response
