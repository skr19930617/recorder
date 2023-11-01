import cv2
from pathlib import Path

output_root = Path("outputs")
output_root.mkdir(exist_ok=True, parents=True)

RECORD_TIME = 5
FPS = 30
def recording(cap, video_writer):
    try:
        loop = int(FPS * RECORD_TIME)
        for i in range(loop):
            _, frame = cap.read()
            video_writer.write(frame)
    except Exception:
        video_writer.release()
        cap.release()
    video_writer.release()
        
def main():
    index = 0
    cap = cv2.VideoCapture(0)
    
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    while True:
        fps = FPS
        w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        name = f"recording_{index}.mp4"
        video_writer = cv2.VideoWriter(str(output_root / name), fourcc, fps, (w,h))
        
        print(f"start {name}")
        recording(cap, video_writer)
        print(f"stop {name}")
        index += 1
    
if __name__ == "__main__":
    main()