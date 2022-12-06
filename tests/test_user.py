from app.main import app
from app import schemas
from fastapi.testclient import TestClient

client = TestClient(app)


def test_root():
    res = client.get("/")
    assert res.json() == {"message": "Hello World!!!"}
    assert res.status_code == 200


def test_create_user():
    res = client.post("/users", json={"email": "example@gmail.com", "password": "12345"})
    user = schemas.UserOut(**res.json())
    assert user.email == "example@gmail.com"
    assert res.status_code == 201
