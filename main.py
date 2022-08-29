import cv2 as cv
import mediapipe as mp
import pyautogui as pg
hand_detector = mp.solutions.hands.Hands()
cap = cv.VideoCapture(0)
draw_utils = mp.solutions.drawing_utils
screen_width, screen_height = pg.size()
index_y = 0
while True:
    _, frame = cap.read()
    frame_height, frame_width, _ = frame.shape
    frame = cv.flip(frame, 1)
    rgb_color = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_color)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            draw_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark
            for id,landmark in enumerate(landmarks):
                x = int(landmark.x * frame_width)
                y = int(landmark.y * frame_height)
                if id == 8:
                    index_x = (screen_width/frame_width)*x
                    index_y = (screen_height/frame_height)*y
                    cv.circle(img=frame, center=(x, y), radius=10, color=(0,255,0))
                    pg.moveTo(index_x, index_y)
                if id == 4:
                    thumb_x = (screen_width / frame_width) * x
                    thumb_y = (screen_height / frame_height) * y
                    cv.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 0))
                    if abs(index_y - thumb_y) < 22:
                        pg.click()
                        pg.sleep(1)
    cv.imshow('virtual mouse', frame)
    cv.waitKey(1)
