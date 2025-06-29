from flask import Blueprint, request, jsonify
from typing import Any
from adroit.auth import token_required, SECRET_KEY, VALID_USERS
import jwt

v1_1_blueprint: Blueprint = Blueprint("v1_1", __name__)


@v1_1_blueprint.route("/add", methods=["GET"])
@token_required
def add_numbers_abs() -> Any:
    a_str: str | None = request.args.get("a")
    b_str: str | None = request.args.get("b")

    if a_str is None or b_str is None:
        return jsonify({"error": "Missing parameters 'a' and 'b'"}), 400

    try:
        a: int = int(a_str)
        b: int = int(b_str)
    except ValueError:
        return jsonify({"error": "Parameters must be integers"}), 400

    result: int = abs(a) + abs(b)
    return jsonify({"result": result}), 200


@v1_1_blueprint.route("/crash", methods=["GET"])
def crash_route() -> None:
    # deliberate bug
    result = 1 / 0
    return jsonify({"result": result})


@v1_1_blueprint.route("/login", methods=["POST"])
def login() -> Any:
    data = request.json
    if not data:
        return jsonify({"error": "Missing JSON body"}), 400
    username = data.get("username")
    password = data.get("password")
    if username == "shane" and password == VALID_USERS.get(username):
        token = jwt.encode({"username": username}, SECRET_KEY, algorithm="HS256")
        return jsonify({"token": token}), 200
    return jsonify({"error": "Invalid credentials"}), 401

