from flask import Flask
from adroit.routes import routes
from adroit.routes import v1_1


def create_app() -> Flask:
    app: Flask = Flask(__name__)
    app.register_blueprint(routes.v1_blueprint, url_prefix="/api/v1")
    app.register_blueprint(v1_1.v1_1_blueprint, url_prefix="/api/v1.1")
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
