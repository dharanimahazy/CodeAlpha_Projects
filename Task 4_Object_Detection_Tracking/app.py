import cv2
from ultralytics import YOLO

def run_object_tracking():
    model = YOLO("yolov8n.pt")

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam video stream.")
        return

    print("YOLO Object Detection and Tracking Started...")
    print("Press 'q' on your keyboard while focusing on the video window to exit.")

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            print("Error: Failed to grab frame from webcam.")
            break

        results = model.track(frame, persist=True)

        annotated_frame = results[0].plot()

        cv2.imshow("CodeAlpha Task 4 - Object Detection & Tracking", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run_object_tracking()
