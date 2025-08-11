from flask import Blueprint, request, jsonify, Response
import cv2
import numpy as np
from ultralytics import YOLO
import base64
import io
from PIL import Image

detection_bp = Blueprint("detection", __name__)

# Load the YOLO model
model = YOLO("yolov8n.pt")

@detection_bp.route("/api/detect", methods=["POST"])
def detect_objects():
    try:
        # Get the image from the request
        data = request.get_json()
        image_data = data["image"]
        
        # Decode base64 image
        image_data = image_data.split(",")[1]  # Remove data:image/jpeg;base64, prefix
        image_bytes = base64.b64decode(image_data)
        image = Image.open(io.BytesIO(image_bytes))
        
        # Convert PIL image to OpenCV format
        opencv_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        
        # Perform object detection
        results = model(opencv_image)
        
        # Process results
        detections = []
        for r in results:
            boxes = r.boxes
            if boxes is not None:
                for box in boxes:
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    conf = float(box.conf[0])
                    cls = int(box.cls[0])
                    label = model.names[cls]
                    
                    detections.append({
                        "bbox": [x1, y1, x2, y2],
                        "confidence": conf,
                        "class": label
                    })
        
        return jsonify({"detections": detections})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@detection_bp.route("/api/detect_video", methods=["POST"])
def detect_video():
    try:
        # This endpoint would handle video file uploads
        # For now, return a placeholder response
        return jsonify({"message": "Video detection endpoint - to be implemented"}) 
    except Exception as e:
        return jsonify({"error": str(e)}), 500

