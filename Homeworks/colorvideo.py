import cv2
import numpy as np

# Capturar video desde la cámara de la laptop
video = cv2.VideoCapture(0)  # El parámetro '0' indica la cámara predeterminada

# Verificar si la cámara fue abierta correctamente
if not video.isOpened():
    print("Error: No se pudo acceder a la cámara.")
else:
    while True:
        # Leer cuadro por cuadro del video de la cámara
        ret, frame = video.read()

        # Si no se puede leer el cuadro, salir del bucle
        if not ret:
            print("Error al capturar el cuadro.")
            break

        # Convertir el cuadro de BGR a HSV
        frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Definir los rangos de color en HSV

        # Rojo (dos rangos)
        bajo_rojo1 = np.array([0, 50, 50])
        alto_rojo1 = np.array([10, 255, 255])
        bajo_rojo2 = np.array([170, 50, 50])
        alto_rojo2 = np.array([180, 255, 255])

        # Verde
        bajo_verde = np.array([40, 50, 50])
        alto_verde = np.array([80, 255, 255])

        # Amarillo
        bajo_amarillo = np.array([20, 50, 50])
        alto_amarillo = np.array([30, 255, 255])

        # Crear máscaras para los colores
        mascara_rojo1 = cv2.inRange(frame_hsv, bajo_rojo1, alto_rojo1)
        mascara_rojo2 = cv2.inRange(frame_hsv, bajo_rojo2, alto_rojo2)
        mascara_rojo = cv2.add(mascara_rojo1, mascara_rojo2)

        mascara_verde = cv2.inRange(frame_hsv, bajo_verde, alto_verde)
        mascara_amarillo = cv2.inRange(frame_hsv, bajo_amarillo, alto_amarillo)

        # Aplicar las máscaras a la imagen capturada
        imagen_rojo = cv2.bitwise_and(frame, frame, mask=mascara_rojo)
        imagen_verde = cv2.bitwise_and(frame, frame, mask=mascara_verde)
        imagen_amarillo = cv2.bitwise_and(frame, frame, mask=mascara_amarillo)

        # Mostrar las imágenes
        cv2.imshow('Imagen Original', frame)
        cv2.imshow('Color Rojo', imagen_rojo)
        cv2.imshow('Color Verde', imagen_verde)
        cv2.imshow('Color Amarillo', imagen_amarillo)

        # Salir del bucle si se presiona la tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Liberar el recurso de la cámara y cerrar las ventanas
    video.release()
    cv2.destroyAllWindows()
