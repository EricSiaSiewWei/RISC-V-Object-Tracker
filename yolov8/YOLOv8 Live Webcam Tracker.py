'''
from ultralytics import YOLO

model = YOLO('bestn.pt')
result = model.predict(source = '/dev/video5', imgsz=640, conf=0.6, show=True)
'''
import cv2
import argparse
import time
from ultralytics import YOLO
import supervision as sv
import numpy as np

def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="YOLOv8 live")
    parser.add_argument(
        "--webcam-resolution", 
        default=[1280, 720], 
        nargs=2, 
        type=int
    )
    args = parser.parse_args()
    return args

def get_correction_signal(detections, frame_width, frame_height):
    if not detections:
        return "none"  # No correction needed if no detections

    detection = detections[0]  # Assuming you are interested in the first detection

    if detection.any():
        box = detection[:4]  # Extract bounding box coordinates

        # Calculate the center of the bounding box
        box_center_x = (box[0] + box[2]) / 2
        box_center_y = (box[1] + box[3]) / 2

        # Calculate the center of the frame
        frame_center_x = frame_width / 2
        frame_center_y = frame_height / 2

        # Calculate the deviation from the center
        deviation_x = box_center_x - frame_center_x
        deviation_y = box_center_y - frame_center_y

        # Define threshold for correction
        threshold = 20

        # Provide correction signals based on deviation
        if abs(deviation_x) > threshold:
            if deviation_x > 0:
                return "right"
            else:
                return "left"
        elif abs(deviation_y) > threshold:
            if deviation_y > 0:
                return "down"
            else:
                return "up"
        else:
            return "middle"  # Signal that the object is in the middle

    else:
        return "none"  # No correction needed if detection is empty

def draw_arrow(frame, direction, start_point, length=30, color=(0, 255, 0), thickness=2):
    # Draw arrow based on the specified direction
    if direction == "up":
        end_point = (start_point[0], start_point[1] - length)
        cv2.arrowedLine(frame, start_point, end_point, color, thickness)
    elif direction == "down":
        end_point = (start_point[0], start_point[1] + length)
        cv2.arrowedLine(frame, start_point, end_point, color, thickness)
    elif direction == "left":
        end_point = (start_point[0] - length, start_point[1])
        cv2.arrowedLine(frame, start_point, end_point, color, thickness)
    elif direction == "right":
        end_point = (start_point[0] + length, start_point[1])
        cv2.arrowedLine(frame, start_point, end_point, color, thickness)

def main():
    args = parse_arguments()
    frame_width, frame_height = args.webcam_resolution

    # Initialize variables for fps calculation
    start_time = time.time()
    frame_count = 0

    #source = "Pipe_Final.mp4"    # 0 denotes Webcam
    source = '/dev/video4'
    cap = cv2.VideoCapture(source, cv2.CAP_V4L2)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)

    model = YOLO("bestn.pt")

    box_annotator = sv.BoxAnnotator(
        thickness=2,
        text_thickness=2,
        text_scale=1
    )

    while (1):
        ret, frame = cap.read()

        result = model(frame, agnostic_nms=True)[0]
        detections = sv.Detections.from_yolov8(result)
        labels = [
            f"{model.model.names[class_id]} {confidence:0.2f}"
            for _, confidence, class_id, _
            in detections
        ]

        correction_signal = "none"  # Default value

        for detection in detections:
            box = detection[:4]  # Extract bounding box coordinates
            correction_signal = get_correction_signal(box, frame_width, frame_height)

            # Apply correction if needed
            if correction_signal != "none":
                print(f"Adjusting: {correction_signal}")
                # Implement your correction logic here

            # Print when the object is in the middle
            if correction_signal == "middle":
                print("Object is in the middle!")

        # Display correction signal on the frame
        cv2.putText(frame, f'Correction: {correction_signal}', (20, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

        # Draw arrow indicators
        draw_arrow(frame, correction_signal, (frame_width // 2, frame_height // 2), length=30)

        frame = box_annotator.annotate(
            scene=frame, 
            detections=detections, 
            labels=labels
        )

        # Calculate fps
        frame_count += 1
        elapsed_time = time.time() - start_time
        fps = frame_count / elapsed_time

        # Display fps in the frame
        cv2.putText(frame, f'FPS: {fps:.2f}', (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)        
        cv2.imshow("YOLO Predictions with FPS", frame)

        # Break the loop if 'q' key is pressed
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break

if __name__ == "__main__":
    main()

