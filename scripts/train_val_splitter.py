import random
import shutil
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent / "data" / "bird"
IMAGES_DIR = BASE_DIR
LABELS_DIR = BASE_DIR / "labels"
OUTPUT_DIR = BASE_DIR

SPLIT_RATIO = 0.8

def split_dataset():
    jpg_files = list(IMAGES_DIR.glob("*.jpg"))
    random.shuffle(jpg_files)

    split_index = int(len(jpg_files) * SPLIT_RATIO)
    train_files = jpg_files[:split_index]
    val_files = jpg_files[split_index:]

    for split_name, files in [("train", train_files), ("val", val_files)]:
        images_out = OUTPUT_DIR / "images" / split_name
        labels_out = OUTPUT_DIR / "labels" / split_name
        images_out.mkdir(parents=True, exist_ok=True)
        labels_out.mkdir(parents=True, exist_ok=True)

        for img_path in files:
            shutil.copy(img_path, images_out / img_path.name)
            label_path = LABELS_DIR / f"{img_path.stem}.txt"
            if label_path.exists():
                shutil.copy(label_path, labels_out / label_path.name)

    print(f"train {len(train_files)}, val{len(val_files)}")

split_dataset()