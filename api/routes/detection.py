import io
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
