from flask.testing import FlaskClient
from adroit.app import create_app
import pytest
from flask import Flask

@pytest.fixture
def client() -> FlaskClient:
    app: Flask = create_app()
    app.config["TESTING"] = True
    return app.test_client()


@pytest.fixture
def token(client: FlaskClient) -> str:
    """Get a valid JWT to use in tests."""
    response = client.post(
        "/api/v1.1/login",
        json={"username": "shane", "password": "my_secret_password"},
    )
    data = response.get_json()
    return data["token"]


def test_add_numbers_abs_positive(client: FlaskClient, token: str) -> None:
    response = client.get(
        "/api/v1.1/add?a=5&b=3",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert response.get_json()["result"] == 8


def test_add_numbers_abs_negative(client: FlaskClient, token: str) -> None:
    response = client.get(
        "/api/v1.1/add?a=-5&b=-7",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert response.get_json()["result"] == 12


def test_add_numbers_abs_mixed(client: FlaskClient, token: str) -> None:
    response = client.get(
        "/api/v1.1/add?a=-4&b=6",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert response.get_json()["result"] == 10


def test_add_numbers_abs_missing_param(client: FlaskClient, token: str) -> None:
    response = client.get(
        "/api/v1.1/add?a=5",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 400
