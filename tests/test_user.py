from app import schemas


def test_root(client):
    res = client.get("/")
    assert res.json() == {"message": "Hello World!!!"}
    assert res.status_code == 200


def test_create_user(client):
    res = client.post("/users", json={"email": "example@gmail.com", "password": "12345"})
    user = schemas.UserOut(**res.json())
    assert user.email == "example@gmail.com"
    assert res.status_code == 201


def test_login(client):
    res = client.post(
        "/login",
        data={"username": "example@gmail.com", "password": "12345"}
    )
    assert res.status_code == 200
