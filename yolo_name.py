from ultralytics import YOLO

modelo = YOLO("yolov8n.pt")

print(modelo.names)