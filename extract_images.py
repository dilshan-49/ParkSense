###########################################################
###   Extract images from videos to make the dataset    ###
###########################################################

import cv2
import os
import numpy as np

# Path to the input video
video_path = 'nr.mp4'  # Replace with your video file path
output_dir = 'my_images'  # Directory to save the extracted images
os.makedirs(output_dir, exist_ok=True)

# Open the video file
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Cannot open video file.")
    exit()

frame_count = 0
frame_skip = 10
while True:
    ret, frame = cap.read()
    if not ret:
        print("End of video or cannot read frame.")
        break
    if frame_count % frame_skip != 0:
        frame_count += 1
        continue    
    # Get original frame dimensions

    h, w, _ = frame.shape

    # Resize while maintaining aspect ratio
    scale = min(640 / w, 640 / h)
    new_w = int(w * scale)
    new_h = int(h * scale)
    resized_frame = cv2.resize(frame, (new_w, new_h))

    # Create a blank 640x640 image and center the resized frame
    padded_frame = np.zeros((640, 640, 3), dtype=np.uint8)
    x_offset = (640 - new_w) // 2
    y_offset = (640 - new_h) // 2
    padded_frame[y_offset:y_offset + new_h, x_offset:x_offset + new_w] = resized_frame

    # Save the padded frame as an image
    name=frame_count//frame_skip
    output_path = os.path.join(output_dir, f"frame_{name:04d}.jpg")
    cv2.imwrite(output_path, padded_frame)
    frame_count += 1

    # Optional: Display the frame (for debugging)
    # cv2.imshow('Frame', padded_frame)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break

cap.release()
cv2.destroyAllWindows()

print(f"Extracted {frame_count} frames and saved to {output_dir}")