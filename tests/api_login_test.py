import pytest

@pytest.mark.smoke
def test_api_health_check(api_client):
    response = api_client.get("/health")
    assert response.status_code == 200

@pytest.mark.regression
def test_api_login(api_client):
    payload = {"username": "testuser", "password": "testpass"}
    response = api_client.post("/api/login", json=payload)
    assert response.status_code == 200
    assert "token" in response.json()