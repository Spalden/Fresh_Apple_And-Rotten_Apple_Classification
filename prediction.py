from ultralytics import YOLO
from PIL import Image
from pathlib import Path
from IPython.display import display

# Load model
model = YOLO("ML_Model/best.pt")

# Input photo in root folder
image_path = "apple.jpg"

# Create output folder
Path("output").mkdir(exist_ok=True)

# Predict on one photo
results = model.predict(
    source=image_path,
    conf=0.25,
    verbose=False
)

# Save detected image
results[0].save(filename="output/apple_detected.jpg")

# Display result
display(Image.open("output/apple_detected.jpg"))

print("Detection completed! Saved to output/apple_detected.jpg")