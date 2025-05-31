import requests

BASE_URL = "http://127.0.0.1:5000"

def test_create_user():
    res = requests.post(f"{BASE_URL}/users", json={"name": "Alice", "email": "alice@example.com"})
    assert res.status_code == 201
    user = res.json()
    assert user["name"] == "Alice"

def test_get_all_users():
    res = requests.get(f"{BASE_URL}/users")
    assert res.status_code == 200
    assert isinstance(res.json(), list)