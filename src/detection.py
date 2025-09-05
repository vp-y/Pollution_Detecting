from ultralytics import YOLO
import cv2
def load_model(weights_path: str):
    return YOLO(weights_path)
def detect_vehicles(model, frame):
    results = model(frame)
    detections = []
    for r in results:
        for box in r.boxes.cpu().numpy():
            x1,y1,x2,y2,conf,cls = box
            if cls == 2:  # class 2 = car in COCO
                detections.append(((int(x1),int(y1),int(x2),int(y2)), float(conf)))
    return detections
if __name__ == "__main__":
    cap = cv2.VideoCapture("../data/videos/test.mp4")
    model = load_model("../models/yolo_weights.pt")
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret: break
        dets = detect_vehicles(model, frame)
        for (x1,y1,x2,y2), conf in dets:
            cv2.rectangle(frame, (x1,y1),(x2,y2),(0,0,255),2)
        cv2.imshow("Detections", frame)
        if cv2.waitKey(1)==27: break
    cap.release()
    cv2.destroyAllWindows()