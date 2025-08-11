import cv2
from ultralytics import YOLO

def detect_objects_in_video(source=0): # source=0 for webcam, or path to video file
    # Load a pretrained YOLOv8n model
    model = YOLO("yolov8n.pt")

    # Open the video source
    cap = cv2.VideoCapture(source)

    if not cap.isOpened():
        print('Error: Could not open video source.')
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Perform object detection on the frame
        results = model(frame, stream=True)  # stream=True for generator

        # Process results and draw bounding boxes
        for r in results:
            boxes = r.boxes  # Boxes object for bbox outputs
            for box in boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                conf = round(float(box.conf[0]), 2)
                cls = int(box.cls[0])
                label = model.names[cls]

                # Draw bounding box and label
                cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2) # Blue color, 2 thickness
                cv2.putText(frame, f'{label} {conf}' , (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

        # Display the frame
        cv2.imshow('Real-Time Object Detection', frame)

        # Break the loop if \'q\' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # To use webcam, set source to 0
    # To use a video file, set source to 'path/to/your/video.mp4'
    detect_objects_in_video(source=0)