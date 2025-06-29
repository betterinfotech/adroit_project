from flask import Blueprint, request, jsonify
from typing import Any
from adroit.auth import token_required

v1_blueprint: Blueprint = Blueprint("v1", __name__)


@v1_blueprint.route("/add", methods=["GET"])
def add_numbers() -> Any:
    a_str: str | None = request.args.get("a")
    b_str: str | None = request.args.get("b")

    if a_str is None or b_str is None:
        return jsonify({"error": "Missing parameters 'a' and 'b'"}), 400

    try:
        a: int = int(a_str)
        b: int = int(b_str)
    except ValueError:
        return jsonify({"error": "Parameters must be integers"}), 400

    result: int = a + b
    return jsonify({"result": result}), 200
