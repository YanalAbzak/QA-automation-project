import requests
from tenacity import retry, stop_after_attempt, wait_fixed

BASE_URL = "http://127.0.0.1:5000"

@retry(stop=stop_after_attempt(5), wait=wait_fixed(2))
def ensure_server_is_running():
    res = requests.get(f"{BASE_URL}/health")
    assert res.status_code == 200

def test_create_user():
    ensure_server_is_running()
    res = requests.post(f"{BASE_URL}/users", json={"name": "Alice", "email": "alice@example.com"})
    assert res.status_code == 201
    user = res.json()
    assert user["name"] == "Alice"

def test_get_all_users():
    ensure_server_is_running()
    res = requests.get(f"{BASE_URL}/users")
    assert res.status_code == 200
    assert isinstance(res.json(), list)