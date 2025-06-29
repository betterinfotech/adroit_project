from flask.testing import FlaskClient
from adroit.app import create_app

def test_add_numbers_success() -> None:
    app = create_app()
    client: FlaskClient = app.test_client()

    response = client.get("/api/v1/add?a=5&b=7")
    json_data = response.get_json()

    assert response.status_code == 200
    assert json_data is not None
    assert json_data["result"] == 12


def test_add_numbers_missing_params() -> None:
    app = create_app()
    client: FlaskClient = app.test_client()

    response = client.get("/api/v1/add?a=5")
    json_data = response.get_json()

    assert response.status_code == 400
    assert json_data is not None
    assert "error" in json_data


def test_add_numbers_invalid_params() -> None:
    app = create_app()
    client: FlaskClient = app.test_client()

    response = client.get("/api/v1/add?a=foo&b=2")
    json_data = response.get_json()

    assert response.status_code == 400
    assert json_data is not None
    assert "error" in json_data
