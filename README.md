# Fresh vs Rotten Apple Detection

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
