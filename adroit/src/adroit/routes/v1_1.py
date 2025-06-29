from flask import Blueprint, request, jsonify
from typing import Any

v1_1_blueprint: Blueprint = Blueprint("v1_1", __name__)


@v1_1_blueprint.route("/add", methods=["GET"])
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

