from pathlib import Path

# ============================================================
# Fresh vs Rotten Apple Detection - Project Structure Generator
# YOLOv8 + FastAPI (inference API) + Flask (web backend)
# + HTML/CSS/JS frontend + Docker + CI/CD + AWS deployment
#
# Architecture:
#   Browser (HTML/CSS/JS)  ->  Flask (web app, port 5000)
#                          ->  FastAPI (YOLOv8 inference, port 8000)
# ============================================================

PROJECT_ROOT = Path(".")

# ============================================================
# DIRECTORIES
# ============================================================

directories = [
    # ML pipeline source
    "src",
    "src/components",
    "src/configuration",
    "src/cloud_storage",
    "src/constants",
    "src/entity",
    "src/exception",
    "src/logger",
    "src/pipeline",
    "src/utils",

    # Data
    "data",
    "data/raw",
    "data/raw/original_apple_images",
    "data/interim",
    "data/interim/resized",
    "data/interim/cleaned",
    "data/interim/augmented",
    "data/processed",
    "data/processed/train/images",
    "data/processed/train/labels",
    "data/processed/val/images",
    "data/processed/val/labels",
    "data/processed/test/images",
    "data/processed/test/labels",
    "data/annotations/train",
    "data/annotations/val",
    "data/annotations/test",
    "data/external",

    # Models
    "models/pretrained",
    "models/production",

    # Artifacts
    "artifacts/runs",
    "artifacts/metrics",
    "artifacts/predictions",

    # Notebook / configs
    "notebooks",
    "configs",

    # FastAPI - inference service
    "api",
    "api/routes",
    "api/schemas",

    # Flask - web backend + HTML/CSS/JS frontend
    "webapp",
    "webapp/routes",
    "webapp/templates",
    "webapp/static/css",
    "webapp/static/js",
    "webapp/static/images",
    "webapp/static/uploads",

    # Scripts / tests
    "scripts",
    "tests",

    # Deployment
    "docker",
    "deployment",
    "deployment/nginx",
    "deployment/aws",

    # CI/CD
    ".github/workflows",
]

# ============================================================
# FILES
# ============================================================

files = [
    # SRC
    "src/__init__.py",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_validation.py",
    "src/components/model_trainer.py",
    "src/components/model_evaluation.py",
    "src/components/model_pusher.py",
    "src/configuration/__init__.py",
    "src/configuration/aws_connection.py",
    "src/cloud_storage/__init__.py",
    "src/cloud_storage/aws_storage.py",
    "src/constants/__init__.py",
    "src/constants/training_constants.py",
    "src/entity/__init__.py",
    "src/entity/config_entity.py",
    "src/entity/artifact_entity.py",
    "src/exception/__init__.py",
    "src/exception/exception.py",
    "src/logger/__init__.py",
    "src/logger/logger.py",
    "src/pipeline/__init__.py",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_pipeline.py",
    "src/utils/__init__.py",
    "src/utils/main_utils.py",
    "src/utils/image_utils.py",

    # Notebook
    "notebooks/FreshApple_and_RottenApple_Classification_Engine.ipynb",

    # Configs
    "configs/training.yaml",
    "configs/inference.yaml",

    # FastAPI
    "api/__init__.py",
    "api/main.py",
    "api/routes/__init__.py",
    "api/routes/detection.py",
    "api/routes/health.py",
    "api/schemas/__init__.py",
    "api/schemas/response.py",

    # Flask
    "webapp/__init__.py",
    "webapp/app.py",
    "webapp/config.py",
    "webapp/routes/__init__.py",
    "webapp/routes/pages.py",
    "webapp/routes/predict.py",
    "webapp/templates/base.html",
    "webapp/templates/index.html",
    "webapp/templates/about.html",
    "webapp/static/css/style.css",
    "webapp/static/js/main.js",
    "webapp/static/images/.gitkeep",
    "webapp/static/uploads/.gitkeep",

    # Scripts
    "scripts/train.py",
    "scripts/evaluate.py",
    "scripts/predict.py",

    # Tests
    "tests/__init__.py",
    "tests/test_model.py",
    "tests/test_api.py",
    "tests/test_webapp.py",

    # Docker
    "docker/Dockerfile.api",
    "docker/Dockerfile.webapp",
    "docker-compose.yml",

    # Deployment
    "deployment/nginx/nginx.conf",
    "deployment/aws/README.md",
    "deployment/gunicorn.conf.py",

    # CI/CD
    ".github/workflows/ci.yml",
    ".github/workflows/cd.yml",

    # Root
    ".env.example",
    ".gitignore",
    ".dockerignore",
    "README.md",
    "requirements.txt",
    "requirements-dev.txt",
    "setup.py",
    "data.yaml",
]

# ============================================================
# STARTER CONTENT
# ============================================================

starter_content = {

    "data.yaml": """path: data/processed

train: train/images
val: val/images
test: test/images

nc: 2

names:
  0: fresh_apple
  1: rotten_apple
""",

    "requirements.txt": """# Core ML / YOLOv8
ultralytics
opencv-python-headless
numpy
Pillow
PyYAML

# FastAPI inference service
fastapi
uvicorn[standard]
python-multipart

# Flask web backend
flask
flask-cors
gunicorn
requests

# AWS / Cloud
boto3
python-dotenv
""",

    "requirements-dev.txt": """-r requirements.txt

# Notebook / Data Science
pandas
matplotlib
seaborn
scikit-learn
ipykernel

# Testing
pytest
httpx

# Code Quality
flake8
""",

    ".env.example": """# AWS
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_REGION=us-east-1
S3_BUCKET_NAME=

# Model
MODEL_PATH=models/production/best.pt
CONF_THRESHOLD=0.25

# Services
FASTAPI_URL=http://localhost:8000
FLASK_SECRET_KEY=change-me
FLASK_DEBUG=1
MAX_UPLOAD_MB=10
""",

    ".gitignore": """__pycache__/
*.py[cod]
.venv/
venv/
env/
.env
.ipynb_checkpoints/

data/raw/
data/interim/
data/processed/
data/annotations/
data/external/

models/
*.pt
*.pth
*.onnx

artifacts/
webapp/static/uploads/*
!webapp/static/uploads/.gitkeep

*.log
.vscode/
.idea/
.DS_Store
Thumbs.db
""",

    ".dockerignore": """.git
.github
__pycache__
*.pyc
.venv
venv
notebooks
tests
data
artifacts
.env
.vscode
.idea
""",

    "README.md": """# Fresh vs Rotten Apple Detection

YOLOv8-based detection of fresh and rotten apples.

## Architecture

    Browser (HTML/CSS/JS) -> Flask (port 5000) -> FastAPI + YOLOv8 (port 8000)

- **FastAPI** (`api/`): loads the YOLOv8 model and exposes `/detect`.
- **Flask** (`webapp/`): serves the HTML/CSS/JS UI and proxies uploads to FastAPI.

## Setup

    python -m venv .venv
    pip install -r requirements-dev.txt
    cp .env.example .env

## Train

    python scripts/train.py

## Run locally (two terminals)

    uvicorn api.main:app --reload --port 8000
    flask --app webapp.app run --debug --port 5000

## Docker

    docker-compose up --build

Open http://localhost:5000
""",

    # ---------------------------------------------------------
    # FASTAPI
    # ---------------------------------------------------------

    "api/main.py": """from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routes import detection, health

app = FastAPI(title="Apple Detection API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router)
app.include_router(detection.router)
""",

    "api/routes/health.py": """from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health():
    return {"status": "ok"}
""",

    "api/routes/detection.py": """import io
import os

from fastapi import APIRouter, File, HTTPException, UploadFile
from PIL import Image

router = APIRouter()

MODEL_PATH = os.getenv("MODEL_PATH", "models/production/best.pt")
CONF = float(os.getenv("CONF_THRESHOLD", "0.25"))

_model = None


def get_model():
    global _model
    if _model is None:
        from ultralytics import YOLO

        _model = YOLO(MODEL_PATH)
    return _model


@router.post("/detect")
async def detect(file: UploadFile = File(...)):
    if not file.content_type or not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Please upload an image file.")

    image = Image.open(io.BytesIO(await file.read())).convert("RGB")
    result = get_model().predict(image, conf=CONF, verbose=False)[0]

    detections = []
    for box in result.boxes:
        cls_id = int(box.cls[0])
        detections.append(
            {
                "label": result.names[cls_id],
                "confidence": round(float(box.conf[0]), 4),
                "bbox": [round(v, 1) for v in box.xyxy[0].tolist()],
            }
        )

    return {
        "count": len(detections),
        "width": image.width,
        "height": image.height,
        "detections": detections,
    }
""",

    "api/schemas/response.py": """from typing import List

from pydantic import BaseModel


class Detection(BaseModel):
    label: str
    confidence: float
    bbox: List[float]


class DetectionResponse(BaseModel):
    count: int
    width: int
    height: int
    detections: List[Detection]
""",

    # ---------------------------------------------------------
    # FLASK
    # ---------------------------------------------------------

    "webapp/config.py": """import os


class Config:
    SECRET_KEY = os.getenv("FLASK_SECRET_KEY", "dev-secret")
    FASTAPI_URL = os.getenv("FASTAPI_URL", "http://localhost:8000")
    MAX_CONTENT_LENGTH = int(os.getenv("MAX_UPLOAD_MB", "10")) * 1024 * 1024
""",

    "webapp/app.py": """from dotenv import load_dotenv
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
""",

    "webapp/routes/pages.py": """from flask import Blueprint, render_template

pages_bp = Blueprint("pages", __name__)


@pages_bp.route("/")
def index():
    return render_template("index.html")


@pages_bp.route("/about")
def about():
    return render_template("about.html")


@pages_bp.route("/healthz")
def healthz():
    return {"status": "ok"}
""",

    "webapp/routes/predict.py": """import requests
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
""",

    "webapp/templates/base.html": """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{% block title %}Apple Detector{% endblock %}</title>
  <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
  <header class="nav">
    <a href="{{ url_for('pages.index') }}" class="brand">Apple Detector</a>
    <nav>
      <a href="{{ url_for('pages.index') }}">Detect</a>
      <a href="{{ url_for('pages.about') }}">About</a>
    </nav>
  </header>
  <main class="container">
    {% block content %}{% endblock %}
  </main>
  <script src="{{ url_for('static', filename='js/main.js') }}"></script>
</body>
</html>
""",

    "webapp/templates/index.html": """{% extends "base.html" %}
{% block content %}
<h1>Fresh or Rotten?</h1>
<p class="muted">Upload an apple photo and the model will tell you.</p>

<form id="upload-form" class="card">
  <input type="file" id="file-input" accept="image/jpeg,image/png,image/webp" required>
  <button type="submit" id="submit-btn">Detect</button>
</form>

<p id="status" class="muted"></p>

<section id="result" class="card hidden">
  <div class="canvas-wrap"><canvas id="canvas"></canvas></div>
  <ul id="detections"></ul>
</section>
{% endblock %}
""",

    "webapp/templates/about.html": """{% extends "base.html" %}
{% block title %}About{% endblock %}
{% block content %}
<h1>About</h1>
<p>YOLOv8 model served via FastAPI, with a Flask web interface.</p>
{% endblock %}
""",

    "webapp/static/css/style.css": """:root {
  --bg: #f7f7f5;
  --card: #ffffff;
  --text: #1c1c1c;
  --muted: #6b6b6b;
  --accent: #2f7d32;
  --bad: #c62828;
}

* { box-sizing: border-box; }

body {
  margin: 0;
  font-family: system-ui, sans-serif;
  background: var(--bg);
  color: var(--text);
}

.nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 14px 24px;
  background: var(--card);
  border-bottom: 1px solid #e5e5e5;
}

.nav a { margin-left: 16px; color: var(--text); text-decoration: none; }
.brand { font-weight: 700; margin-left: 0 !important; }

.container { max-width: 760px; margin: 32px auto; padding: 0 16px; }
.muted { color: var(--muted); }
.hidden { display: none; }

.card {
  background: var(--card);
  border: 1px solid #e5e5e5;
  border-radius: 10px;
  padding: 16px;
  margin-top: 16px;
}

button {
  margin-left: 8px;
  padding: 8px 18px;
  border: 0;
  border-radius: 6px;
  background: var(--accent);
  color: #fff;
  cursor: pointer;
}

button:disabled { opacity: 0.6; cursor: wait; }

.canvas-wrap canvas { max-width: 100%; height: auto; border-radius: 6px; }
#detections { padding-left: 18px; }
""",

    "webapp/static/js/main.js": """const form = document.getElementById("upload-form");

if (form) {
  const input = document.getElementById("file-input");
  const btn = document.getElementById("submit-btn");
  const status = document.getElementById("status");
  const result = document.getElementById("result");
  const list = document.getElementById("detections");
  const canvas = document.getElementById("canvas");
  const ctx = canvas.getContext("2d");

  const COLORS = { fresh_apple: "#2f7d32", rotten_apple: "#c62828" };

  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const file = input.files[0];
    if (!file) return;

    btn.disabled = true;
    status.textContent = "Analyzing...";
    result.classList.add("hidden");

    const body = new FormData();
    body.append("file", file);

    try {
      const res = await fetch("/api/predict", { method: "POST", body });
      const data = await res.json();
      if (!res.ok) throw new Error(data.error || "Request failed");

      await draw(file, data);
      render(data);
      status.textContent = "";
      result.classList.remove("hidden");
    } catch (err) {
      status.textContent = err.message;
    } finally {
      btn.disabled = false;
    }
  });

  function draw(file, data) {
    return new Promise((resolve) => {
      const img = new Image();
      img.onload = () => {
        canvas.width = img.width;
        canvas.height = img.height;
        ctx.drawImage(img, 0, 0);
        ctx.lineWidth = Math.max(2, img.width / 200);
        ctx.font = `${Math.max(14, img.width / 40)}px sans-serif`;

        data.detections.forEach((d) => {
          const [x1, y1, x2, y2] = d.bbox;
          const color = COLORS[d.label] || "#1565c0";
          ctx.strokeStyle = color;
          ctx.fillStyle = color;
          ctx.strokeRect(x1, y1, x2 - x1, y2 - y1);
          ctx.fillText(`${d.label} ${(d.confidence * 100).toFixed(0)}%`, x1 + 4, Math.max(16, y1 - 6));
        });
        resolve();
      };
      img.src = URL.createObjectURL(file);
    });
  }

  function render(data) {
    list.innerHTML = "";
    if (data.count === 0) {
      list.innerHTML = "<li>No apples detected.</li>";
      return;
    }
    data.detections.forEach((d) => {
      const li = document.createElement("li");
      li.textContent = `${d.label} - ${(d.confidence * 100).toFixed(1)}%`;
      list.appendChild(li);
    });
  }
}
""",

    # ---------------------------------------------------------
    # DOCKER / DEPLOYMENT
    # ---------------------------------------------------------

    "docker/Dockerfile.api": """FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends libgl1 libglib2.0-0 \\
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src ./src
COPY api ./api
COPY models/production ./models/production

EXPOSE 8000
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
""",

    "docker/Dockerfile.webapp": """FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir flask flask-cors gunicorn requests python-dotenv

COPY webapp ./webapp
COPY deployment/gunicorn.conf.py ./gunicorn.conf.py

EXPOSE 5000
CMD ["gunicorn", "-c", "gunicorn.conf.py", "webapp.app:app"]
""",

    "docker-compose.yml": """services:
  api:
    build:
      context: .
      dockerfile: docker/Dockerfile.api
    env_file: .env
    ports:
      - "8000:8000"
    healthcheck:
      test: ["CMD", "python", "-c", "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')"]
      interval: 30s
      timeout: 5s
      retries: 3

  webapp:
    build:
      context: .
      dockerfile: docker/Dockerfile.webapp
    env_file: .env
    environment:
      FASTAPI_URL: http://api:8000
    ports:
      - "5000:5000"
    depends_on:
      - api

  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
    volumes:
      - ./deployment/nginx/nginx.conf:/etc/nginx/nginx.conf:ro
    depends_on:
      - webapp
""",

    "deployment/gunicorn.conf.py": """bind = "0.0.0.0:5000"
workers = 2
timeout = 120
accesslog = "-"
errorlog = "-"
""",

    "deployment/nginx/nginx.conf": """events {}

http {
  client_max_body_size 10M;

  server {
    listen 80;

    location / {
      proxy_pass http://webapp:5000;
      proxy_set_header Host $host;
      proxy_set_header X-Real-IP $remote_addr;
      proxy_read_timeout 120s;
    }
  }
}
""",

    "deployment/aws/README.md": """# AWS Deployment Notes

1. Create an ECR repository for each image (`apple-api`, `apple-webapp`).
2. Push images (the CD workflow does this on merge to main).
3. Run on EC2 with docker-compose, or ECS/Fargate with two services:
   - `api` (port 8000, internal only)
   - `webapp` (port 5000, behind an ALB or nginx)
4. Set `FASTAPI_URL` on the webapp to the internal address of the api service.
5. Store the model (`best.pt`) in S3 and download it at container start,
   or bake it into the api image.
""",

    # ---------------------------------------------------------
    # CI/CD
    # ---------------------------------------------------------

    ".github/workflows/ci.yml": """name: CI

on:
  push:
    branches: [main]
  pull_request:

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: pip install -r requirements-dev.txt
      - run: flake8 src api webapp --max-line-length 120
      - run: pytest -q
""",

    ".github/workflows/cd.yml": """name: CD

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: aws-actions/configure-aws-credentials@v4
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: ${{ secrets.AWS_REGION }}

      - id: ecr
        uses: aws-actions/amazon-ecr-login@v2

      - name: Build and push images
        run: |
          docker build -f docker/Dockerfile.api -t ${{ steps.ecr.outputs.registry }}/apple-api:latest .
          docker build -f docker/Dockerfile.webapp -t ${{ steps.ecr.outputs.registry }}/apple-webapp:latest .
          docker push ${{ steps.ecr.outputs.registry }}/apple-api:latest
          docker push ${{ steps.ecr.outputs.registry }}/apple-webapp:latest
""",

    # ---------------------------------------------------------
    # TESTS
    # ---------------------------------------------------------

    "tests/test_api.py": """from fastapi.testclient import TestClient

from api.main import app

client = TestClient(app)


def test_health():
    assert client.get("/health").json() == {"status": "ok"}
""",

    "tests/test_webapp.py": """from webapp.app import create_app


def test_index_and_health():
    client = create_app().test_client()
    assert client.get("/").status_code == 200
    assert client.get("/healthz").json == {"status": "ok"}
""",
}

# ============================================================
# DATA README FILES
# ============================================================

data_readmes = {
    "data/raw/README.md": "# Raw Data\n\nStore the original, unmodified apple images here.\n",
    "data/interim/README.md": "# Interim Data\n\nResized, cleaned and augmented images generated during preprocessing.\n",
    "data/processed/README.md": (
        "# Processed YOLO Dataset\n\n"
        "processed/\n"
        "|-- train/{images,labels}\n"
        "|-- val/{images,labels}\n"
        "`-- test/{images,labels}\n"
    ),
    "data/annotations/README.md": "# Annotations\n\nYOLO label format:\n\nclass_id x_center y_center width height\n",
    "data/external/README.md": "# External Data\n\nStore external or downloaded datasets here.\n",
}

# ============================================================
# CREATE
# ============================================================

print("=" * 70)
print("CREATING PROJECT DIRECTORIES")
print("=" * 70)

for directory in directories:
    path = PROJECT_ROOT / directory
    path.mkdir(parents=True, exist_ok=True)
    print(f"[DIR]    {path}")

print()
print("=" * 70)
print("CREATING PROJECT FILES")
print("=" * 70)

for file in files:
    path = PROJECT_ROOT / file
    path.parent.mkdir(parents=True, exist_ok=True)

    if not path.exists():
        path.touch()
        print(f"[FILE]   {path}")
    else:
        print(f"[EXISTS] {path}")

    if file in starter_content and path.stat().st_size == 0:
        path.write_text(starter_content[file], encoding="utf-8")
        print("         -> Starter content written")

print()
print("=" * 70)
print("CREATING DATA DOCUMENTATION")
print("=" * 70)

for file, content in data_readmes.items():
    path = PROJECT_ROOT / file
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        print(f"[FILE]   {path}")
    else:
        print(f"[EXISTS] {path}")

print()
print("=" * 70)
print("PROJECT STRUCTURE CREATED SUCCESSFULLY")
print("=" * 70)
print(f"Project root: {PROJECT_ROOT.resolve()}")
print("""
Next steps:
1. python -m venv .venv && pip install -r requirements-dev.txt
2. cp .env.example .env
3. Put images in data/raw/original_apple_images/ and prepare YOLO labels
4. Put the final dataset in data/processed/ and run: python scripts/train.py
5. Copy best.pt to models/production/
6. Start FastAPI : uvicorn api.main:app --reload --port 8000
7. Start Flask   : flask --app webapp.app run --debug --port 5000
8. Or run all    : docker-compose up --build   (http://localhost)
""")