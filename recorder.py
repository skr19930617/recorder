import cv2
from pathlib import Path

RECORD_TIME = 3600
FPS = 30
def recording(name):
    output_root = Path("outputs")
    output_root.mkdir(exist_ok=True, parents=True)
    cap = cv2.VideoCapture(0)
    fps = FPS
    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    video = cv2.VideoWriter(str(output_root / name), fourcc, fps, (w,h))
 
    print(f"recording start {name}")
    loop = int(fps * RECORD_TIME)
    for i in range(loop):
        _, frame = cap.read()
        video.write(frame)
    print(f"recording stop {name}")
    video.release()
    cap.release()
    return video

index = 0
is_recording = True
while is_recording:
    try:
        recording(f"recording_{index}.mp4")
        index += 1
    except Exception:
        is_recording = False