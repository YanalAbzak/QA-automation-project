import requests

BASE_URL = "http://127.0.0.1:5000"

def test_invalid_user_creation():
    res = requests.post(f"{BASE_URL}/users", json={"email": "missingname@example.com"})
    assert res.status_code != 201

def test_delete_nonexistent_user():
    res = requests.delete(f"{BASE_URL}/users/9999")
    assert res.status_code == 404