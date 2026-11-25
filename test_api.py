from fastapi.testclient import TestClient

from api import app

client = TestClient(app)


def test_hello():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, FastAPI!"}


def test_hello_with_name():
    response = client.get("/hello", params={"name": "Константин"})
    assert response.status_code == 200
    assert response.json() == {"message": "Привет, Константин!"}


def test_missing_name():
    assert client.get("/hello").status_code == 422
