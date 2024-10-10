from ultralytics import YOLO

# Load a pretrained YOLO11n model
model = YOLO("./runs/detect/train/weights/last.pt")

# Define path to directory containing images and videos for inference
source = "./predict_test_videos"

# Run inference on the source
results = model(source, stream=True)  # generator of Results objects