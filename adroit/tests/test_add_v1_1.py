from flask.testing import FlaskClient
from adroit.app import create_app

def test_add_numbers_abs_positive() -> None:
    app = create_app()
    client: FlaskClient = app.test_client()
    response = client.get("/api/v1.1/add?a=5&b=3")
    data = response.get_json()
    assert response.status_code == 200
    assert data is not None
    assert data["result"] == 8

def test_add_numbers_abs_negative() -> None:
    app = create_app()
    client: FlaskClient = app.test_client()
    response = client.get("/api/v1.1/add?a=-5&b=-7")
    data = response.get_json()
    assert response.status_code == 200
    assert data is not None
    assert data["result"] == 12  # abs(-5) + abs(-7)

def test_add_numbers_abs_mixed() -> None:
    app = create_app()
    client: FlaskClient = app.test_client()
    response = client.get("/api/v1.1/add?a=-4&b=6")
    data = response.get_json()
    assert response.status_code == 200
    assert data is not None
    assert data["result"] == 10  # abs(-4) + abs(6)

def test_add_numbers_abs_missing_param() -> None:
    app = create_app()
    client: FlaskClient = app.test_client()
    response = client.get("/api/v1.1/add?a=5")
    data = response.get_json()
    assert response.status_code == 400
    assert data is not None
    assert "error" in data
