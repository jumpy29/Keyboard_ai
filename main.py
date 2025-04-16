import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)   #0 is webcam id
cap.set(3, 1280)    #3-width map, 1280 width
cap.set(4, 720)     #4-height map, 720 height

while True:
    #next 3 lines for running webcam
    success, img = cap.read()
    cv2.imshow("Image", img)
    cv2.waitKey(1)  #1ms
