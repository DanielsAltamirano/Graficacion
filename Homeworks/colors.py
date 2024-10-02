import cv2
import numpy as np

# Ruta de la imagen
ruta_imagen = r'C:\Users\Daniels\Desktop\graficacion\Recursos\manzanascolors.jpg'

# Leer la imagen
imagen = cv2.imread(ruta_imagen)

# Verificar si la imagen fue cargada correctamente
if imagen is None:
    print("Error: No se pudo cargar la imagen. Verifica la ruta y el nombre del archivo.")
else:
    # Convertir la imagen de BGR a HSV
    imagen_hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

    # Definir los rangos de color en HSV

    # Rojo (dos rangos por el ciclo de color)
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
    mascara_rojo1 = cv2.inRange(imagen_hsv, bajo_rojo1, alto_rojo1)
    mascara_rojo2 = cv2.inRange(imagen_hsv, bajo_rojo2, alto_rojo2)
    mascara_rojo = cv2.add(mascara_rojo1, mascara_rojo2)

    mascara_verde = cv2.inRange(imagen_hsv, bajo_verde, alto_verde)
    mascara_amarillo = cv2.inRange(imagen_hsv, bajo_amarillo, alto_amarillo)

    # Aplicar las máscaras a la imagen original
    imagen_rojo = cv2.bitwise_and(imagen, imagen, mask=mascara_rojo)
    imagen_verde = cv2.bitwise_and(imagen, imagen, mask=mascara_verde)
    imagen_amarillo = cv2.bitwise_and(imagen, imagen, mask=mascara_amarillo)

    # Mostrar las imágenes
    cv2.imshow('Imagen Original', imagen)
    cv2.imshow('Color Rojo', imagen_rojo)
    cv2.imshow('Color Verde', imagen_verde)
    cv2.imshow('Color Amarillo', imagen_amarillo)

    # Esperar a que se pulse una tecla para cerrar las ventanas
    cv2.waitKey(0)
    cv2.destroyAllWindows()
