#!/usr/bin/env python3
"""Documentation String"""
#Jose Santiago
#Apr 14, 2020

#Import Libraries
import numpy as np
import cv2

#Opening IP Camera Stream 
cap = cv2.VideoCapture('http://x.x.x.x:8080/video')


while True:

    #Capture Frame-by-Frame
    ret, frame = cap.read()
    #Change to gray
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Display the frame of VideoCapture
    cv2.imshow("Capturing",frame)
    #Wait for quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#Release Capture and Destroy Windows when finished
cap.release()
cv2.destroyAllWindows()
