import numpy as np
import cv2 as cv

# Iniciar captura de video y verificar
cap = cv.VideoCapture(0)
if not cap.isOpened(): exit()

# Parámetros y configuración inicial
frame_width, frame_height = int(cap.get(3)), int(cap.get(4))
lk_params = dict(winSize=(15, 15), maxLevel=2, criteria=(cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 0.03))
ret, first_frame = cap.read()
if not ret: exit()

first_frame = cv.flip(first_frame, 1)
prev_gray = cv.cvtColor(first_frame, cv.COLOR_BGR2GRAY)
ball_pos = np.array([[[frame_width // 2, frame_height // 2]]], dtype=np.float32)
rect = (50, 50, frame_width - 50, frame_height - 50)

while True:
    ret, frame = cap.read()
    if not ret: break

    frame = cv.flip(frame, 1)
    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    new_ball_pos, _, _ = cv.calcOpticalFlowPyrLK(prev_gray, gray_frame, ball_pos, None, **lk_params)

    if new_ball_pos is not None:
        a, b = new_ball_pos.ravel()
        if not (rect[0] < a < rect[2] and rect[1] < b < rect[3]):
            new_ball_pos = np.array([[[frame_width // 2, frame_height // 2]]], dtype=np.float32)
        ball_pos = new_ball_pos
        frame = cv.circle(frame, (int(a), int(b)), 20, (0, 255, 0), -1)

    frame = cv.rectangle(frame, rect[:2], rect[2:], (255, 0, 0), 5)
    cv.imshow('Pelota en movimiento', frame)
    prev_gray = gray_frame

    if cv.waitKey(30) & 0xFF == 27: break

cap.release()
cv.destroyAllWindows()
