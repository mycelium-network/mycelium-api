from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "status": "running",
        "swagger_ui": "/docs",
        "redoc": "/redoc",
        "openid_connect": "/.well-known/openid-configuration"
        }