import jwt
from flask import request, jsonify
from functools import wraps
from typing import Any, Callable

SECRET_KEY = "supersecretjwtkey123"

VALID_USERS = {"shane": "my_secret_password"}

def token_required(f: Callable) -> Callable:
    @wraps(f)
    def decorated(*args: Any, **kwargs: Any) -> Any:
        auth = request.headers.get("Authorization")
        if not auth or not auth.startswith("Bearer "):
            return jsonify({"error": "Missing or invalid Authorization header"}), 401
        try:
            token = auth.split()[1]
            payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            if payload.get("username") != "shane":
                return jsonify({"error": "User not allowed"}), 403
        except jwt.InvalidTokenError:
            return jsonify({"error": "Invalid token"}), 403
        return f(*args, **kwargs)
    return decorated
