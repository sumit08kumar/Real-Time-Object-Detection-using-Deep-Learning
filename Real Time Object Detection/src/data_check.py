import os
from ultralytics import YOLO

# Define the path to the dataset
dataset_path = '../data/datasets/coco128'

# Verify if the dataset path exists
if os.path.exists(dataset_path):
    print(f"Dataset found at: {dataset_path}")
    
    # Optionally, load a YOLO model and try to access dataset info
    try:
        model = YOLO('yolov8n.pt') # Load a pretrained YOLOv8n model
        # This will try to load the dataset info if coco128.yaml is correctly configured
        # For coco128, the data is usually auto-detected by Ultralytics if placed correctly
        print("Attempting to load dataset info via YOLO model...")
        # A dummy train call to verify data loading and configuration
        # This will not actually train, but will check data integrity
        model.train(data='coco128.yaml', epochs=1, imgsz=640, mode='detect', device='cpu')
        print("Dataset loaded successfully by YOLO.")
    except Exception as e:
        print(f"Error loading dataset with YOLO: {e}")
else:
    print(f"Dataset not found at: {dataset_path}")
    print("Please ensure coco128 dataset is downloaded and extracted to the correct path.")


