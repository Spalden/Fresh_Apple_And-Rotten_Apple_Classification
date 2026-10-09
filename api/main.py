from fastapi import FastAPI
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
