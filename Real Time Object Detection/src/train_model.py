from ultralytics import YOLO

# Load a pretrained YOLOv8n model
model = YOLO('yolov8n.pt')

# Train the model on the coco128 dataset for a few epochs
# The dataset will be automatically downloaded if not present
results = model.train(data='coco128.yaml', epochs=5, imgsz=640, device='cpu')

print("Training complete. Results saved to runs/detect/train")


