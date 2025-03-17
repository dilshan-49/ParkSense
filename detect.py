############################################################
#        Testing the trained model on sample videos        #
############################################################


#import cv2
import os
#import supervision as sv
from ultralytics import YOLO
import numpy as np

HOME=os.getcwd()
model = YOLO('model/best.pt')





input_video = 'video/test.mp4'  # Path to the input video
output_video = 'output_with_predictions.mp4'  # Path to save the output video

model.predict(source=input_video, save=True, save_txt=False, save_conf=False, project='.', name='output/best', vid_stride=1, device=0)



# box_annotator=sv.BoundingBoxAnnotator()
# label_annotator=sv.LabelAnnotator()
# cap=cv2.VideoCapture('demo.mp4')





# if not cap.isOpened():
#     print("Cannot open camera")
#     exit()

# output_dir = 'output_imgs'
# os.makedirs(output_dir, exist_ok=True)

# img_counter=0

# while True:
#     ret, frame = cap.read()

#     if not ret:
#         print("Can't receive frame (stream end?). Exiting ...")
#         break
#     frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)  # Rotate 90 degrees clockwise

#     #resized_frame = cv2.resize(frame, (640, 640))
#     h, w, _ = frame.shape

#     # Calculate scale and padding to maintain aspect ratio
#     scale = min(640 / w, 640 / h)
#     new_w = int(w * scale)
#     new_h = int(h * scale)
#     resized_frame = cv2.resize(frame, (new_w, new_h))

#     # Create a blank 640x640 image and center the resized frame
#     padded_frame = np.zeros((640, 640, 3), dtype=np.uint8)
#     x_offset = (640 - new_w) // 2
#     y_offset = (640 - new_h) // 2
#     padded_frame[y_offset:y_offset + new_h, x_offset:x_offset + new_w] = resized_frame



#     results = model(padded_frame)[0]
#     detections=sv.Detections.from_ultralytics(results)

#     annotated_frame= box_annotator.annotate(padded_frame,detections)
#     annotated_frame= label_annotator.annotate(annotated_frame,detections)

#     cv2.imshow('video',annotated_frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()