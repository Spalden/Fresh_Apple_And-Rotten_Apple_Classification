from typing import List

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
