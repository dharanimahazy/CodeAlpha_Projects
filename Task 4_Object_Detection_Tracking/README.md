CodeAlpha_Object_Detection_Tracking

A real-time Computer Vision application designed to process live video streams, detect individual objects, and actively track them across sequential video frames. This project utilizes the state-of-the-art YOLOv8 architecture alongside OpenCV, fulfilling Task 4 of the CodeAlpha Artificial Intelligence Internship program.

Features
- Real-Time Processing: Connects natively to local system hardware webcams to capture high frame-rate input.
- Object Detection: Utilizes deep learning convolutional layers to accurately draw labeled bounding boxes around items.
- Multi-Object Tracking: Implements continuous observation logic to persist and maintain unique tracking IDs for every element on screen.
- Dynamic Annotation: Overlays real-time classification labels and matching confidence statistics dynamically onto the frame view.

Tech Stack & Dependencies
- Core Engine: Python 3.x
- Computer Vision Framework: OpenCV
- Deep Learning Architecture: Ultralytics YOLOv8

Local Installation & Setup

1. Navigate to the Directory:
   cd "Task 4_Object_Detection_Tracking"

2. Install Required Extensions:
   pip install -r requirements.txt

3. Run Application Runtime:
   python app.py

Internship Details
- Organization: CodeAlpha
- Domain: Artificial Intelligence Internship
- Task Assignment: Task 4 — Object Detection and Tracking