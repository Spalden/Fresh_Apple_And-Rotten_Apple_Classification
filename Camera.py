
from ultralytics import YOLO
import cv2

# Load trained YOLO model
model = YOLO("ML_Model/best.pt")

# Print model classes
print("Model classes:", model.names)

# Open default webcam
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("Error: Could not open camera.")
    raise SystemExit(1)

print("Camera started!")
print("Press 'q' to quit.")

try:
    while True:
        ret, frame = cap.read()

        if not ret:
            print("Failed to capture frame.")
            break

        # Run YOLO prediction
        results = model.predict(
            source=frame,
            conf=0.25,
            verbose=False
        )

        # Draw bounding boxes and labels
        annotated_frame = results[0].plot()

        # Display webcam detection
        cv2.imshow(
            "Apple Freshness Detection",
            annotated_frame
        )

        # Quit when q is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

finally:
    cap.release()
    cv2.destroyAllWindows()

print("Detection stopped.")
