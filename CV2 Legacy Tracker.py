'''
Author: Eric Sia Siew Wei
Background: Bechelor of Electrical & Electronics Engineering (Hons.), Universiti Teknologi PETRONAS (UTP)
Project: Development of Object Tracking System on a RISC-V Embedded System Platform
Subject: OpenCV Legacy Tracker
'''

import cv2
import time

source = 0    # 0 denotes Webcam
cap = cv2.VideoCapture(source)
tracker = cv2.legacy_TrackerMOSSE.create()

#Supported Trackers:
'''
            +---------------------------------------------------|-------------------------------------------------------+
            | Tracker                                           | Syntax          					|
            |---------------------------------------------------|-------------------------------------------------------|
            | MOSSE (Minimum Output Sum of Squared Error)       | tracker = cv2.legacy_TrackerMOSSE.create()           	|
            | TLD (Tracking, Learning and Detection)		| tracker = cv2.legacy_TrackerTLD.create()   		|
            | MIL          					| tracker = cv2.legacy_TrackerMIL.create()          	|
            | Median Flow       				| tracker = cv2.legacy_TrackerMedianFlow.create()  	|
            | KCF (Kernelized Correlation Filter)              	| tracker = cv2.legacy_TrackerKCF.create()           	|
            | CSRT                				| tracker = cv2.legacy_TrackerCSRT.create()        	|
            | Boosting             				| tracker = cv2.legacy_TrackerBoosting.create()       	|
            +---------------------------------------------------|-------------------------------------------------------+

'''

trackable, fr = cap.read()
bounding_box = cv2.selectROI("Select Object to Track (Press Enter to Start)", fr, False)
tracker.init(fr, bounding_box)
start_time = time.time()
frame_count = 0

def BoundBox(image, bounding_box):
    x, y, w, h = int(bounding_box[0]), int(bounding_box[1]), int(bounding_box[2]), int(bounding_box[3])
    cv2.rectangle(image, (x, y), ((x + w), (y + h)), (255, 0, 255), 3, 3 )
    cv2.putText(image, "Tracking", (210, 85), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    
while(1):
    timer = cv2.getTickCount()
    trackable, image = cap.read()
    trackable, bounding_box = tracker.update(image)
    if trackable:
        BoundBox(image,bounding_box)
    else:
        cv2.putText(image, "Lost", (210, 85), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    frame_count += 1
    elapsed_time = time.time() - start_time
    fps = frame_count / elapsed_time
    cv2.putText(image, f'FPS: {fps:.2f}', (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2);
    cv2.putText(image, "Tracking Status:", (20, 85), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2) 
    cv2.imshow("RISC-V OpenCV Legacy Tracker", image)
    if cv2.waitKey(1) & 0xff == ord('q'):
       break
