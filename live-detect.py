import cv2
from ultralytics import YOLO
from PIL import Image
from datetime import datetime
import matplotlib.pyplot as plt
from twilio.rest import Client

# Load the models
phone_model = YOLO("phone.pt")
face_model = YOLO("face.pt")

# Class names for phone.pt model
phone_classes = ["person_with_phone", "person_without_phone"]
face_classes = ["Anubhab", "Aritra", "Sharnabho", "Trisgani"]

# Corresponding phone numbers for each face class
phone_numbers = {
    "Anubhab": "+919123608110",
    "Aritra": "+917980608326",
    "Sharnabho": "+917044908614",
    "Trisgani": "+917439618940"
}

# Twilio configuration
account_sid = 'ACbe27f7a5690073b37f0a3f322bf027ac'
auth_token = 'cad2253e0817965959df69e29b417f16'
twilio_phone_number = '+12085564659'

client = Client(account_sid, auth_token)

# Function to send SMS
def send_sms(to, message):
    client.messages.create(
        body=message,
        from_=twilio_phone_number,
        to=to
    )

# Function to run detection and log results
def run_detection(frame, log_file):
    # Convert the frame to PIL image
    image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    
    # Run detection with phone model
    phone_results = phone_model(image)
    
    with open(log_file, 'a') as log:
        for result in phone_results:
            for box in result.boxes:
                class_id = int(box.cls)
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                class_name = phone_classes[class_id]
                log.write(f"{timestamp} - Detected class {class_name} in bounding box {x1, y1, x2, y2}\n")
                
                # Draw bounding box and label on the frame
                color = (255, 0, 0) if class_id == 0 else (0, 255, 0)
                cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
                cv2.putText(frame, class_name, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)
                
                # If the detected class is 'person_with_phone', run face detection
                if class_id == 0:
                    cropped_image = image.crop((x1, y1, x2, y2))
                    face_results = face_model(cropped_image)
                    
                    for face_result in face_results:
                        for face_box in face_result.boxes:
                            face_class_id = int(face_box.cls)
                            face_class_name = face_classes[face_class_id]
                            log.write(f"{timestamp} - Detected face {face_class_name} in bounding box {x1, y1, x2, y2}\n")
                            
                            # Draw bounding box and label on the frame
                            fx1, fy1, fx2, fy2 = map(int, face_box.xyxy[0])
                            fx1 += x1
                            fy1 += y1
                            fx2 += x1
                            fy2 += y1
                            cv2.rectangle(frame, (fx1, fy1), (fx2, fy2), (0, 255, 255), 2)
                            cv2.putText(frame, face_class_name, (fx1, fy1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 255), 2)
                            
                            # Send SMS to the corresponding phone number
                            if face_class_name in phone_numbers:
                                message = f"Detected {face_class_name} at {timestamp}"
                                send_sms(phone_numbers[face_class_name], message)

# Example usage
log_file = "detection_log.txt"

# Open a connection to the webcam
cap = cv2.VideoCapture(1)

plt.ion()  # Turn on interactive mode
fig, ax = plt.subplots()

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Run detection on the current frame
    run_detection(frame, log_file)
    
    # Convert frame to RGB for matplotlib
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Display the frame with detections
    ax.clear()
    ax.imshow(frame_rgb)
    plt.draw()
    plt.pause(0.001)
    
    # Break the loop if 'q' is pressed
    if plt.waitforbuttonpress(0.001):
        break

# Release the webcam and close the window
cap.release()
plt.close()