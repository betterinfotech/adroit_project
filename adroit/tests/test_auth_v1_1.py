import pytest
from flask import Flask
from typing import Generator
from adroit.app import create_app


@pytest.fixture
def client() -> Generator:
    app: Flask = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_valid_login(client) -> None:
    response = client.post(
        "/api/v1.1/login",
        json={"username": "shane", "password": "my_secret_password"},
    )
    assert response.status_code == 200
    data = response.get_json()
    assert "token" in data
    assert isinstance(data["token"], str)


def test_invalid_login(client) -> None:
    response = client.post(
        "/api/v1.1/login",
        json={"username": "shane", "password": "wrong_password"},
    )
    assert response.status_code == 401
    data = response.get_json()
    assert "error" in data


def test_missing_credentials(client) -> None:
    response = client.post("/api/v1.1/login", json={})
    assert response.status_code == 400
    data = response.get_json()
    assert "error" in data


def test_protected_route_with_valid_token(client) -> None:
    # login first
    login_response = client.post(
        "/api/v1.1/login",
        json={"username": "shane", "password": "my_secret_password"},
    )
    token = login_response.get_json()["token"]

    # use token to access protected add
    protected_response = client.get(
        "/api/v1.1/add?a=2&b=-4",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert protected_response.status_code == 200
    data = protected_response.get_json()
    assert data["result"] == 6  # abs(2) + abs(-4)


def test_protected_route_with_missing_token(client) -> None:
    response = client.get("/api/v1.1/add?a=2&b=-4")
    assert response.status_code == 401
    data = response.get_json()
    assert "error" in data


def test_protected_route_with_invalid_token(client) -> None:
    response = client.get(
        "/api/v1.1/add?a=2&b=-4",
        headers={"Authorization": "Bearer faketoken"},
    )
    assert response.status_code == 403
    data = response.get_json()
    assert "error" in data
