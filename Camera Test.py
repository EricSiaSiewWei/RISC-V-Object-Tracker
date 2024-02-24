import cv2
import time
import cProfile

def display_video(video_path):
    cap = cv2.VideoCapture(video_path, cv2.CAP_V4L2)
    #cap = cv2.VideoCapture(video_path)
    cap.set(cv2.CAP_PROP_FPS, desired_fps)
    if not cap.isOpened():
        print("Error: Could not open video file.")
        return
    frame_count = 0
    start_time = time.time()
    while True:
        ret, frame = cap.read()
        frame = cv2.resize(frame, (640, 480))
        if not ret:
            print("Video has ended.")
            break
        cv2.imshow('Video', frame)
        frame_count += 1
        current_time = time.time()
        if current_time - start_time >= 1.0:
            calculated_fps = frame_count / (current_time - start_time)
            print(f"Calculated frame rate: {calculated_fps} frames per second")
            frame_count = 0
            start_time = current_time
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
video_file_path = '/dev/video4'
desired_fps = 15
display_video(video_file_path)
cProfile.run('display_video')

