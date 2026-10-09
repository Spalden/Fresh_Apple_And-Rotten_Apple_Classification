import requests
from flask import Blueprint, current_app, jsonify, request

predict_bp = Blueprint("predict", __name__)

ALLOWED = {"image/jpeg", "image/png", "image/webp"}


@predict_bp.route("/predict", methods=["POST"])
def predict():
    file = request.files.get("file")
    if file is None or file.filename == "":
        return jsonify(error="No file uploaded."), 400
    if file.mimetype not in ALLOWED:
        return jsonify(error="Only JPG, PNG or WEBP images are allowed."), 400

    try:
        resp = requests.post(
            f"{current_app.config['FASTAPI_URL']}/detect",
            files={"file": (file.filename, file.stream, file.mimetype)},
            timeout=60,
        )
        resp.raise_for_status()
    except requests.RequestException as exc:
        return jsonify(error=f"Inference service error: {exc}"), 502

    return jsonify(resp.json())
