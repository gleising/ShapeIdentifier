#import numpy as np
import cv2
import os
import time
from src import detect_shapes

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()  # ret = 1 if the video is captured; frame is the image
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    detect_shapes.shapeFinder(frame)
    # Display the resulting image
    cv2.imshow('Video Capture', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):  # press q to quit
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
