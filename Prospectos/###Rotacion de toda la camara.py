###Rotacion de toda la camara 
import numpy as np
import cv2 as cv
import mediapipe as mp

# Inicialización de Mediapipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

# Iniciar captura de video y verificar
cap = cv.VideoCapture(0)
if not cap.isOpened():
    exit()

# Parámetros iniciales
frame_width, frame_height = int(cap.get(3)), int(cap.get(4))
ball_pos = np.array([frame_width // 2, frame_height // 2])
ball_radius = 20
rotation_angle = 0

# Puntos rojos iniciales para rotación
point1 = np.array([100, 100])  # Punto fijo
point2 = np.array([200, 100])  # Punto móvil

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv.flip(frame, 1)
    rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Obtener coordenadas de puntos clave
            index_finger = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            middle_finger = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
            palm_base = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST]

            # Convertir a coordenadas de pantalla
            index_pos = np.array([int(index_finger.x * frame_width), int(index_finger.y * frame_height)])
            middle_pos = np.array([int(middle_finger.x * frame_width), int(middle_finger.y * frame_height)])
            palm_pos = np.array([int(palm_base.x * frame_width), int(palm_base.y * frame_height)])

            # Traslación: La bola sigue la palma
            ball_pos = palm_pos

            # Escalamiento: Cambiar radio en función de la distancia entre índice y medio
            distance_fingers = np.linalg.norm(index_pos - middle_pos)
            ball_radius = max(10, min(100, int(distance_fingers)))

            # Actualizar punto2 (móvil) con la posición del dedo índice
            point2 = index_pos

            # Rotación: Cambiar ángulo según la distancia entre los puntos rojos
            current_distance = np.linalg.norm(point1 - point2)
            if current_distance > 150:
                rotation_angle += 2  # Rotar en sentido horario
            elif current_distance < 100:
                rotation_angle -= 2  # Rotar en sentido antihorario

    # Dibujar la bola verde con rotación
    rotation_center = (int(ball_pos[0]), int(ball_pos[1]))  # Asegurar tuple de enteros
    rotation_matrix = cv.getRotationMatrix2D(rotation_center, rotation_angle, 1)
    rotated_frame = cv.warpAffine(frame, rotation_matrix, (frame_width, frame_height))
    cv.circle(rotated_frame, rotation_center, ball_radius, (0, 255, 0), -1)

    # Dibujar puntos rojos para rotación
    cv.circle(frame, tuple(point1), 10, (0, 0, 255), -1)  # Punto fijo
    cv.circle(frame, tuple(point2), 10, (0, 0, 255), -1)  # Punto móvil

    # Mostrar el marco con los puntos y la bola rotada
    cv.imshow('Control de Bola', rotated_frame)
    cv.imshow('Vista Original', frame)

    # Salir con la tecla ESC
    if cv.waitKey(30) & 0xFF == 27:
        break

cap.release()
cv.destroyAllWindows()
