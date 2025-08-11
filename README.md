# Real-Time-Object-Detection-using-Deep-Learning

# Real-Time Object Detection using YOLOv8

A comprehensive end-to-end real-time object detection system built with YOLOv8, featuring both command-line and web interfaces for detecting objects in images and videos.

## 🚀 Features

- **Real-Time Processing**: Uses optimized YOLOv8 model for fast object detection
- **Multiple Object Detection**: Identifies 80 different object classes from the COCO dataset
- **Bounding Box Visualization**: Displays bounding boxes with class labels and confidence scores
- **Web Interface**: Modern web application for easy interaction
- **Video Processing**: Supports both live camera feeds and video file processing
- **Pre-trained Models**: Uses COCO pre-trained YOLOv8 weights for immediate deployment

## 📋 Table of Contents

- [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Technical Details](#technical-details)
- [Performance](#performance)
- [Contributing](#contributing)
- [License](#license)

## 🛠️ Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager
- OpenCV compatible system

### Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd real_time_object_detection
```

2. Install dependencies:
```bash
pip install ultralytics opencv-python numpy matplotlib flask Pillow
```

3. Download sample data (optional):
```bash
# Sample video will be downloaded automatically when running the detection script
```

## 📁 Project Structure

```
real_time_object_detection/
├── data/
│   ├── datasets/
│   │   └── coco128/          # COCO128 dataset for training/testing
│   └── sample_video.mp4      # Sample video for testing
├── models/                   # Trained model storage
├── src/
│   ├── detect_objects.py     # Main detection script
│   ├── train_model.py        # Model training script
│   └── data_check.py         # Data validation script
├── web/
│   └── object_detection_web/ # Flask web application
│       ├── src/
│       │   ├── routes/       # API routes
│       │   ├── static/       # Frontend files
│       │   └── main.py       # Flask app entry point
│       └── requirements.txt
├── static/                   # Static assets
├── templates/                # HTML templates
└── README.md
```

## 🎯 Usage

### Command Line Interface

#### Basic Object Detection on Video

```bash
python src/detect_objects.py
```

This will process the sample video and display real-time object detection results.

#### Custom Video Processing

```python
from src.detect_objects import detect_objects_in_video

# Process custom video file
detect_objects_in_video("path/to/your/video.mp4")

# Use webcam (if available)
detect_objects_in_video(0)
```

### Web Interface

1. Navigate to the web application directory:
```bash
cd web/object_detection_web
```

2. Activate virtual environment:
```bash
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the Flask application:
```bash
python src/main.py
```

5. Open your browser and navigate to `http://localhost:5000`

## 📡 API Documentation

### POST /api/detect

Detect objects in a single image.

**Request Body:**
```json
{
  "image": "data:image/jpeg;base64,<base64-encoded-image>"
}
```

**Response:**
```json
{
  "detections": [
    {
      "bbox": [x1, y1, x2, y2],
      "confidence": 0.85,
      "class": "person"
    }
  ]
}
```

### POST /api/detect_video

Process video files for object detection (endpoint for future implementation).

## 🔧 Technical Details

### Model Architecture

- **Base Model**: YOLOv8n (Nano version for optimal speed/accuracy balance)
- **Input Size**: 640x640 pixels
- **Classes**: 80 COCO dataset classes
- **Framework**: Ultralytics YOLOv8

### Supported Object Classes

The system can detect 80 different object classes including:
- People and animals (person, cat, dog, horse, etc.)
- Vehicles (car, truck, bus, motorcycle, bicycle, etc.)
- Household items (chair, table, TV, laptop, etc.)
- Food items (apple, banana, pizza, etc.)
- Sports equipment (ball, racket, etc.)

### Performance Metrics

- **Model Size**: ~6MB (YOLOv8n)
- **Parameters**: 3.2M
- **Speed**: Varies based on hardware (CPU vs GPU)
- **Accuracy**: mAP50-95: 37.3% on COCO validation set

## 🚀 Performance

### Hardware Requirements

**Minimum:**
- CPU: Intel i5 or equivalent
- RAM: 4GB
- Storage: 1GB free space

**Recommended:**
- CPU: Intel i7 or equivalent
- RAM: 8GB+
- GPU: NVIDIA GTX 1060 or better (for GPU acceleration)
- Storage: 2GB+ free space

### Optimization Tips

1. **GPU Acceleration**: Install CUDA and PyTorch with GPU support for faster inference
2. **Model Selection**: Use YOLOv8s or YOLOv8m for better accuracy, YOLOv8n for speed
3. **Input Resolution**: Lower input resolution (e.g., 320x320) for faster processing
4. **Batch Processing**: Process multiple images in batches for efficiency

## 🎨 Customization

### Training on Custom Dataset

1. Prepare your dataset in YOLO format
2. Update the dataset configuration
3. Run training:

```python
from ultralytics import YOLO

model = YOLO("yolov8n.pt")
results = model.train(data="your_dataset.yaml", epochs=100, imgsz=640)
```

### Modifying Detection Parameters

```python
# Adjust confidence threshold
results = model(image, conf=0.5)

# Adjust IoU threshold for NMS
results = model(image, iou=0.7)

# Specify classes to detect
results = model(image, classes=[0, 1, 2])  # person, bicycle, car only
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Ultralytics](https://ultralytics.com/) for the YOLOv8 implementation
- [COCO Dataset](https://cocodataset.org/) for training data
- [OpenCV](https://opencv.org/) for computer vision utilities
- [Flask](https://flask.palletsprojects.com/) for web framework

## 📞 Support

For support, please open an issue in the GitHub repository.

---

**Built with ❤️ using YOLOv8 and modern web technologies**

