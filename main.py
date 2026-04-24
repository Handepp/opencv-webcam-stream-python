import cv2
import json

# Load config file
with open("config.json", "r") as file:
    config = json.load(file)

CAMERA_INDEX = config["camera_index"]
FRAME_WIDTH = config["frame_width"]
FRAME_HEIGHT = config["frame_height"]
WINDOW_NAME = config["window_name"]

cap = cv2.VideoCapture(CAMERA_INDEX, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("Could not open webcam")
    exit()

cap.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)

print("Press 'q' to exit")

while True:
    ret, frame = cap.read()
    
    if not ret:
        print("Failed to read frame")
        break

    # Get actual frame dimensions
    actual_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    actual_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    cv2.imshow(WINDOW_NAME, frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()