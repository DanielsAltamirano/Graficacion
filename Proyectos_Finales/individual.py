# Importar librerías necesarias
import numpy as np  # Manipulación de arrays y operaciones matemáticas.
import cv2 as cv    # Procesamiento de imágenes y video.
import mediapipe as mp  # Detección de manos y puntos clave.

# Inicialización de los módulos de Mediapipe para detección de manos.
mp_hands = mp.solutions.hands  # Solución de Mediapipe para detección y seguimiento de manos.
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)  # Configuración de los parámetros de confianza mínima.
mp_drawing = mp.solutions.drawing_utils  # Utilidad para dibujar los puntos detectados.

# Iniciar captura de video desde la cámara (índice 0 para la cámara predeterminada).
cap = cv.VideoCapture(0)
if not cap.isOpened():  # Verificar que la cámara está funcionando.
    exit()  # Salir del programa si no hay acceso a la cámara.

# Configuración inicial de parámetros.
frame_width, frame_height = int(cap.get(3)), int(cap.get(4))  # Dimensiones del cuadro capturado.
ball_pos = np.array([frame_width // 2, frame_height // 2])  # Posición inicial de la bola (centro del marco).
ball_radius = 20  # Radio inicial de la bola.
rotation_angle = 0  # Ángulo inicial de rotación.

# Inicialización de dos puntos rojos para calcular rotación.
point1 = np.array([100, 100])
point2 = np.array([200, 100])

# Bucle principal para procesar el video en tiempo real.
while True:
    ret, frame = cap.read()  # Leer un cuadro de video.
    if not ret:  # Salir del bucle si no se captura un cuadro.
        break

    frame = cv.flip(frame, 1)  # Voltear el cuadro horizontalmente (espejo).
    rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)  # Convertir el cuadro de BGR a RGB para Mediapipe.
    results = hands.process(rgb_frame)  # Procesar el cuadro para detectar manos.

    if results.multi_hand_landmarks:  # Si se detectan manos en el cuadro.
        for hand_landmarks in results.multi_hand_landmarks:
            # Obtener coordenadas de los puntos clave: punta del índice, punta del medio y base de la palma.
            index_finger = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            middle_finger = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
            palm_base = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST]

            # Convertir coordenadas relativas a valores absolutos en el marco.
            index_pos = np.array([int(index_finger.x * frame_width), int(index_finger.y * frame_height)])
            middle_pos = np.array([int(middle_finger.x * frame_width), int(middle_finger.y * frame_height)])
            palm_pos = np.array([int(palm_base.x * frame_width), int(palm_base.y * frame_height)])

            # Actualizar la posición de la bola para que siga la palma de la mano.
            ball_pos = palm_pos

            # Ajustar el radio de la bola en función de la distancia entre el índice y el medio.
            distance_fingers = np.linalg.norm(index_pos - middle_pos)
            ball_radius = max(10, min(100, int(distance_fingers)))  # Restringir el radio entre 10 y 100.

            # Calcular el ángulo de rotación según la distancia entre los puntos rojos.
            point1 = index_pos
            current_distance = np.linalg.norm(point1 - point2)
            if current_distance > 150:
                rotation_angle += 2  # Incrementar el ángulo para rotar en sentido horario.
            elif current_distance < 100:
                rotation_angle -= 2  # Decrementar el ángulo para rotar en sentido antihorario.

    # Dibujar una bola verde con rotación alrededor del centro.
    rotation_center = (int(ball_pos[0]), int(ball_pos[1]))  # Centro de la rotación (coordenadas de la bola).
    rotation_matrix = cv.getRotationMatrix2D(rotation_center, rotation_angle, 1)  # Matriz de transformación de rotación.
    rotated_ball = cv.circle(np.zeros((frame_height, frame_width, 3), dtype=np.uint8), rotation_center, ball_radius, (0, 255, 0), -1)  # Dibujar la bola.
    rotated_ball = cv.warpAffine(rotated_ball, rotation_matrix, (frame_width, frame_height))  # Aplicar rotación a la bola.
    frame = cv.addWeighted(frame, 1, rotated_ball, 1, 0)  # Combinar el cuadro original con la bola rotada.

    # Dibujar los puntos rojos usados para calcular rotación.
    cv.circle(frame, tuple(point1), 10, (0, 0, 255), -1)  # Dibujar punto 1.
    cv.circle(frame, tuple(point2), 10, (0, 0, 255), -1)  # Dibujar punto 2.

    # Mostrar el cuadro procesado.
    cv.imshow('Control de Bola', frame)

    # Salir si se presiona la tecla ESC.
    if cv.waitKey(30) & 0xFF == 27:
        break

# Liberar recursos y cerrar ventanas.
cap.release()
cv.destroyAllWindows()
