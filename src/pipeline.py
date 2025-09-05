import cv2
from detection import load_model, detect_vehicles
from ocr import init_reader, recognize_plate
from database import init_db, log_record
from alerts import send_alert

def main(video_path: str, email_recipient: str):
    init_db()
    model = load_model("../models/yolo_weights.pt")
    reader = init_reader()
    cap = cv2.VideoCapture(video_path)
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret: break
        dets = detect_vehicles(model, frame)
        for bbox, conf in dets:
            plate = recognize_plate(reader, frame, bbox)
            log_record(plate, conf)
            if conf > 0.9:
                send_alert(plate, conf, email_recipient)
        cv2.waitKey(1)
    
    cap.release()

if __name__ == "__main__":
    main("../data/videos/test.mp4", "enforcement@city.gov")