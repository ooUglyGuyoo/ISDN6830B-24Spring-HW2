from ultralytics import YOLO

# Create a new YOLO model from scratch
model = YOLO('yolov8n.yaml')

# Load a pretrained YOLO model (recommended for training)
# model = YOLO('yolov8n.pt')

print("=====================START TRAINING=====================")
# Train the model using the dataset for epochs
results = model.train(data='/workspace/6830-HW2-data/data.yaml', epochs=100)

print("=====================START VALIDATION=====================")
# Evaluate the model's performance on the validation set
results = model.val()

# print("=====================Perform on image=====================")
# Perform object detection on an image using the model
# results = model.predict('test.jpg')

# Export the model to ONNX format
success = model.export(format='onnx')