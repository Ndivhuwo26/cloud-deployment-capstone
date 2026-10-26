import pytest
from app.app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as test_client:
        yield test_client


def test_homepage(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.json["service"] == "cloud-deployment-capstone"
    assert response.json["status"] == "running"


def test_health_endpoint(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json["status"] == "healthy"
    assert response.json["service"] == "cloud-deployment-capstone"
