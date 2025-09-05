import easyocr
import cv2
def init_reader():
    return easyocr.Reader(['en'], gpu=True)
def recognize_plate(reader, image, bbox):
    x1,y1,x2,y2 = bbox
    crop = image[y1:y2, x1:x2]
    result = reader.readtext(crop)
    text = result[0][1] if result else ""
    return text