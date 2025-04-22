import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)   #0 is webcam id
cap.set(3, 1280)    #3-width map, 1280 width
cap.set(4, 720)     #4-height map, 720 height

detector = HandDetector(detectionCon=0.8)   #only detect hand if confidence is at least 80%
keys = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
        ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";"],
        ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/"]]


def drawAll(img, buttonList):
    for button in buttonList:
        x, y = button.pos
        w, h = button.size

        cv2.rectangle(img, button.pos, (x+w, y+h), (255, 0, 255), cv2.FILLED)
        cv2.putText(img, button.text, (x+20, y+65), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)

    return img


class Button():
    def __init__(self, pos, text, size=[85, 85]):
        self.pos = pos
        self.text = text
        self.size = size

    
buttonList = []
for i in range(len(keys)):
    for x, key in enumerate(keys[i]):
        buttonList.append(Button([100*x+50, 100*i+50], key))


while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)
    img = drawAll(img, buttonList)

    if hands:
        for hand in hands:
            lmList = hand["lmList"]
            for button in buttonList:
                x, y = button.pos
                w, h = button.size

                if x < lmList[8][0] < x+w and y < lmList[8][1] < y+h:
                    cv2.rectangle(img, button.pos, (x+w, y+h), (175, 0, 175), cv2.FILLED)
                    cv2.putText(img, button.text, (x+20, y+65), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
                    length, info, img = detector.findDistance(lmList[8][0:2], lmList[12][0:2], img)
                    if length<40:
                        cv2.rectangle(img, button.pos, (x+w, y+h), (0, 255, 0), cv2.FILLED)
                        cv2.putText(img, button.text, (x+20, y+65), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)

    cv2.imshow("Image", img)
    cv2.waitKey(1)  #1ms  