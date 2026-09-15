from pathlib import Path

LABELS_DIR = Path(__file__).parent.parent / "data" / "bird" / "labels"

def fix_class_id(labels_dir):
    for txt_file in labels_dir.glob("*.txt"):
        with open(txt_file, "r") as f:
            lines = f.readlines()
            for i in range(len(lines)):
                tokens = lines[i].split()
                tokens[0] = "0"
                lines[i] = " ".join(tokens)
            lines = "\n".join(lines)

        with open(txt_file, "w") as f:
            f.write(lines)

fix_class_id(LABELS_DIR)