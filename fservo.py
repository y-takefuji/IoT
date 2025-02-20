# original:https://github.com/pdhruv93/computer-vision/tree/main/fingers-count
# original is modified by takefuji
# arduino IDE->File->Examples->Firmata->StandardFirmata should be installed.
import mediapipe as mp
import cv2
import math
import numpy as np
import os
import serial
import pyfirmata
from time import sleep
b=pyfirmata.Arduino('COM3')
it = pyfirmata.util.Iterator(b)
it.start()
pin = b.get_pin('d:2:s')
#b.digital[2].write(90)
pin.write(90)

Hands = mp.solutions.hands
Draw = mp.solutions.drawing_utils

class HandDetector:
    def __init__(self, max_num_hands=2, min_detection_confidence=0.5, min_tracking_confidence=0.5):
        self.hands = Hands.Hands(max_num_hands=max_num_hands, min_detection_confidence=min_detection_confidence,
                                   min_tracking_confidence=min_tracking_confidence)

    def findHandLandMarks(self, image, handNumber=0, draw=False):
        originalImage = image
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # mediapipe needs RGB
        results = self.hands.process(image)
        landMarkList = []

        if results.multi_handedness:
            label = results.multi_handedness[handNumber].classification[0].label  # label gives if hand is left or right
            #account for inversion in cam
            if label == "Left":
                label = "Right"
            elif label == "Right":
                label = "Left"

        if results.multi_hand_landmarks:  # returns None if hand is not found
            hand = results.multi_hand_landmarks[handNumber] #results.multi_hand_landmarks returns landMarks for all the hands

            for id, landMark in enumerate(hand.landmark):
                # landMark holds x,y,z ratios of single landmark
                imgH, imgW, imgC = originalImage.shape  # height, width, channel for image
                xPos, yPos = int(landMark.x * imgW), int(landMark.y * imgH)
                landMarkList.append([id, xPos, yPos, label])

            if draw:
                Draw.draw_landmarks(originalImage, hand, Hands.HAND_CONNECTIONS)
        return landMarkList


handDetector = HandDetector(min_detection_confidence=0.7)

def main():
 ledstate=0
 cam = cv2.VideoCapture(0)
 while True:
    status, image = cam.read()
    image =cv2.flip(image,1)
    handLandmarks = handDetector.findHandLandMarks(image=image, draw=True)
    count=0
    x=0
    y=0
    if(len(handLandmarks) != 0):
# handLandmarks[point of 21 points][x or y] locates finger positions.
# see details: https://google.github.io/mediapipe/solutions/hands
# handLandmarks[4][1] 4->Thumb_tip 1->x-axis
# handLandmarks[8][2] 8->Index_finger_tip 2->y-axis

        if handLandmarks[4][1]+50 < handLandmarks[5][1]:       #Thumb finger
            count = count+1
        if handLandmarks[8][2] < handLandmarks[6][2]:       #Index finger
            count = count+1
        if handLandmarks[12][2] < handLandmarks[10][2]:     #Middle finger
            count = count+1
        if handLandmarks[16][2] < handLandmarks[14][2]:     #Ring finger
            count = count+1
        if handLandmarks[20][2] < handLandmarks[18][2]:     #Little finger
            count = count+1
        x=int(handLandmarks[8][1]/3)
        y=handLandmarks[8][2]
    cv2.putText(image, str(count), (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 5, (255, 0, 0), 25)
    cv2.putText(image, "x="+str(x), (85, 125), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 5)
    cv2.putText(image, "y="+str(y), (245, 125), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 5)
    if x<1:x=1
    if x>255:x=255
    b.digital[2].write(x)
    cv2.imshow("result", image)
    cv2.moveWindow("result",10,10)
    cv2.setWindowProperty("result", cv2.WND_PROP_TOPMOST, 1)    
    if cv2.waitKey(1) == ord('q'):
     cam.release()
     cv2.destroyWindow("result")
     break


if __name__ == '__main__':
 main()
 os._exit(0) 

