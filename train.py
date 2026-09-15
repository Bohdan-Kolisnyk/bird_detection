from pathlib import Path
from ultralytics import YOLO

def train():
    data_yaml = Path(__file__).parent / "data" / "bird" / "data.yaml"
    model = YOLO("yolo26n.pt")
    model.train(data=str(data_yaml), epochs=100, imgsz=640, batch=16, name="first_run")

if __name__ == "__main__":
    train()