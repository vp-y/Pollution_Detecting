import smtplib
from email.message import EmailMessage
import os
def send_alert(plate: str, conf: float, recipient: str):
    msg = EmailMessage()
    msg['Subject'] = f"Polluting Vehicle Detected: {plate}"
    msg['From'] = os.getenv('ALERT_EMAIL')
    msg['To'] = recipient
    msg.set_content(f"Vehicle {plate} detected with confidence {conf:.2f}.")
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(os.getenv('ALERT_EMAIL'), os.getenv('ALERT_PASS'))
        smtp.send_message(msg)