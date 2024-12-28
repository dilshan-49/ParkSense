import cv2
import pytesseract
import configparser
import os

config = configparser.ConfigParser()
config_path = os.path.join(os.path.dirname(__file__), 'config.ini')
print(f"Reading config file from: {config_path}")
config.read(config_path)
# Debug: Print sections and keys
print("Sections:", config.sections())
print("DEFAULT keys:", config['DEFAULT'].keys())


droidcam_url = config['DEFAULT']['DroidCamURL']  # URL of the DroidCam video stream

# Initialize video capture from DroidCam
cap = cv2.VideoCapture(droidcam_url)

if not cap.isOpened():
    print("Error: Could not open video stream from DroidCam.")
    exit()

frame_count = 0
while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break

    # Save the frame to disk
    frame_path = f'frame_{frame_count}.jpg'
    cv2.imwrite(frame_path, frame)
    print(f"Saved frame to {frame_path}")

    # Perform OCR on the frame
    text = pytesseract.image_to_string(frame)
    print("Detected text:", text)

    frame_count += 1

    # Exit after processing a certain number of frames
    if frame_count >= 10:
        break

# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
