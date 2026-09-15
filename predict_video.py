import argparse
import cv2
from ultralytics import YOLO
import time

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="шлях до вхідного відео")
    parser.add_argument("--output", required=True, help="шлях для збереження результату")
    parser.add_argument("--weights", default="weights/best.pt")
    return parser.parse_args()

def process_video(input_path, output_path, weights_path):
    model = YOLO(weights_path)

    cap = cv2.VideoCapture(input_path)
    if not cap.isOpened():
        print("no video")
        return

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    writer = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    frame_count = 0
    start_time = time.time()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame_count += 1

        results = model(frame, verbose=False, conf=0.5)
        plot_res = results[0].plot()
        writer.write(plot_res)

        if frame_count % 30 == 0:
            tot_time= time.time() - start_time
            print(f"processed {frame_count}/{total_frames} frames in {tot_time:.1f}s")

    cap.release()
    writer.release()
    print(f"frames {frame_count}")
    print(f"output in {output_path}")

if __name__ == "__main__":
    args = parse_args()
    process_video(args.input, args.output, args.weights)