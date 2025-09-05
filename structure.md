``` pollution-vehicle-id/
 data/                     # Sample test images/videos
 frames/                   # Extracted video frames
 videos/                   # Raw surveillance footage
 models/                   # YOLOv8 and OCR checkpoints
 yolo_weights.pt           # YOLOv8 trained weights
 ocr_model/                # EasyOCR model files
 src/
 __init__.py
 detection.py              # YOLOv8 inference on frames
 ocr.py                    # EasyOCR plate recognition
 database.py               # DB schema and logging functions
 alerts.py                 # Automated alert generation
 pipeline.py               # Orchestrator for real-time pipeline
 requirements.txt          # Python dependencies
 README.md                 # Project overview & setup
 ``
