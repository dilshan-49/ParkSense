# ParkSense

This repository contains the implementation of a **Parking Management System** built using a Raspberry Pi. The system captures images of vehicles entering or exiting a parking area, extracts their license plate numbers using Optical Character Recognition (OCR), and records the details in a database for efficient management.

## Features
- **Raspberry Pi Integration**: Utilizes Raspberry Pi to control the system, capture images, and process data.
- **License Plate Detection**: Automatically extracts license plate numbers from captured images using OCR.
- **Entry/Exit Logging**: Maintains a record of vehicles entering and exiting the parking area.
- **Database Management**: Stores license plate numbers with timestamps in a database for tracking and reporting.

## Components
### Hardware
- Raspberry Pi (any model with GPIO and camera module support)
- Smartphone camera (using DroidCam or equivalent as an external camera)
- Sensor (e.g., IR or ultrasonic) to detect vehicle presence

### Software
- Python 3
- OpenCV (for image processing)
- Tesseract OCR (for license plate recognition)
- SQLite or any preferred database (for data storage)

## System Workflow
1. **Vehicle Detection**: A sensor detects when a vehicle stops at the entry/exit point.
2. **Image Capture**: The Raspberry Pi triggers the camera to capture an image.
3. **License Plate Recognition**:
   - Processes the image using OpenCV.
   - Extracts the license plate number using Tesseract OCR.
4. **Database Logging**: Stores the license plate number, entry/exit status, and timestamp in a database.
