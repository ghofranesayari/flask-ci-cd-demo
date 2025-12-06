import pytest
from app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.testing = True
    with app.test_client() as client:
        yield client


def test_health_ok(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_message_endpoint(client):
    response = client.get("/message")
    assert response.status_code == 200
    data = response.get_json()
    assert "message" in data
    assert isinstance(data["message"], str)


def test_echo_endpoint(client):
    payload = {"hello": "world"}
    response = client.post("/echo", json=payload)
    assert response.status_code == 200
    data = response.get_json()
    assert data["received"] == payload
