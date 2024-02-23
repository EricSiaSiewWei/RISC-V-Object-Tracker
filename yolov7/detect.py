import argparse
import time
from pathlib import Path

import cv2
import torch
import torch.backends.cudnn as cudnn
from numpy import random

from models.experimental import attempt_load
from utils.datasets import LoadStreams, LoadImages
from utils.general import check_img_size, check_requirements, check_imshow, non_max_suppression, apply_classifier, \
    scale_coords, xyxy2xywh, strip_optimizer, set_logging, increment_path
from utils.plots import plot_one_box
from utils.torch_utils import select_device, load_classifier, time_synchronized, TracedModel


def get_correction_signal(detections, frame_width, frame_height):
    if detections.numel() == 0:
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


def detect(source, weights, device, img_size, iou_thres, conf_thres):
    #webcam = source.isnumeric() 

    # Initialize
    set_logging()
    frame_count = 0
    start_time = time.time()
    device = select_device(device)
    half = device.type != 'cpu'  # half precision only supported on CUDA

    # Load model
    model = attempt_load(weights, map_location=device)  # load FP32 model
    stride = int(model.stride.max())  # model stride
    imgsz = check_img_size(img_size, s=stride)  # check img_size

    if half:
        model.half()  # to FP16

    # Convert the model to quantized version
    model = torch.quantization.quantize_dynamic(model, {torch.nn.Linear}, dtype=torch.qint8)
    

    # Set Dataloader
    #if webcam:
    view_img = check_imshow()
    cudnn.benchmark = True  # set True to speed up constant image size inference
    dataset = LoadStreams(source, img_size=imgsz, stride=stride)

    # Get names and colors
    names = model.module.names if hasattr(model, 'module') else model.names
    colors = [[random.randint(0, 255) for _ in range(3)] for _ in names]

    # TorchScript
    model = model.fuse().eval()

    # Run inference
    if device.type != 'cpu':
        model(torch.zeros(1, 3, imgsz, imgsz).to(device).type_as(next(model.parameters())))  # run once
    old_img_w = old_img_h = img_size
    old_img_b = 1

    t0 = time.perf_counter()
    for path, img, im0s, vid_cap in dataset:
        img = torch.from_numpy(img).to(device)
        img = img.half() if half else img.float()  # uint8 to fp16/32
        img /= 255.0  # 0 - 255 to 0.0 - 1.0
        if img.ndimension() == 3:
            img = img.unsqueeze(0)

        # Warmup
        if device.type != 'cpu' and (old_img_b != img.shape[0] or old_img_h != img.shape[2] or old_img_w != img.shape[3]):
            old_img_b = img.shape[0]
            old_img_h = img.shape[2]
            old_img_w = img.shape[3]

        # Inference
        t1 = time_synchronized()
        with torch.no_grad():
            pred = model(img)
        t2 = time_synchronized()

        # Apply NMS
        # Assuming the first element of the tuple is the predicted tensor
        pred = pred[0] if isinstance(pred, tuple) and len(pred) > 0 else pred
        pred = non_max_suppression(pred, conf_thres, iou_thres)
        t3 = time_synchronized()

        # Process detections
        for i, det in enumerate(pred):  # detections per image
            #if webcam:  # batch_size >= 1
            p, s, im0, frame = path[i], '%g: ' % i, im0s[i].copy(), dataset.count
            p = Path(p)  # to Path
            gn = torch.tensor(im0.shape)[[1, 0, 1, 0]]  # normalization gain whwh
            if len(det):
                # Rescale boxes from img_size to im0 size
                det[:, :4] = scale_coords(img.shape[2:], det[:, :4], im0.shape).round()

                # Print results
                for c in det[:, -1].unique():
                    n = (det[:, -1] == c).sum()  # detections per class
                    s += f"{n} {names[int(c)]}{'s' * (n > 1)}, "  # add to string

                # Write results
                for *xyxy, conf, cls in reversed(det):
                    label = f'{names[int(cls)]} {conf:.2f}'
                    plot_one_box(xyxy, im0, label=label, color=colors[int(cls)], line_thickness=2)
                        # Get correction signal
            correction_signal = get_correction_signal(det, im0.shape[1], im0.shape[0])

            # Draw arrow based on correction signal
            if correction_signal != "none":
                arrow_start_point = (int(im0.shape[1] / 2), int(im0.shape[0] / 2))
                draw_arrow(im0, correction_signal, arrow_start_point)

                # Print correction signal
                print(f'Correction Signal: {correction_signal}')

            # Calculate fps
            frame_count += 1
            elapsed_time = time.time() - start_time
            fps = frame_count / elapsed_time

            # Display fps in the frame
            cv2.putText(im0, f'FPS: {fps:.2f}', (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.putText(im0, f'Correction: {correction_signal}', (20, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
            cv2.imshow(str(p), im0)
    print(f'Done. ({time.perf_counter() - t0:.3f}s)')
    
if __name__ == '__main__':
    weights_path = r"/home/user/Documents/FYP_19000760/yolov7/runs/train/exp3/weights/best.pt"
    #weights_path = "yolov7.pt"
    #source = '/dev/video4, cv2.CAP_V4L2'
    #source = 'http://192.168.137.118:81/stream'
    source = '/dev/video4'
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    print(device)
    with torch.no_grad():
        detect(source, weights_path, device, img_size = 100, iou_thres = 0.45, conf_thres = 0.6)

