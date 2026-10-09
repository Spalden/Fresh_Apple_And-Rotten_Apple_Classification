from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS

load_dotenv()

from webapp.config import Config  # noqa: E402
from webapp.routes.pages import pages_bp  # noqa: E402
from webapp.routes.predict import predict_bp  # noqa: E402


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)

    app.register_blueprint(pages_bp)
    app.register_blueprint(predict_bp, url_prefix="/api")
    return app


app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
