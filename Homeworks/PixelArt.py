import cv2
import numpy as np

# Cargar la imagen
ruta_imagen = 'C:/Users/Daniels/Desktop/graficacion/Recursos/SharinganMadara.svg.png'
imagen = cv2.imread(ruta_imagen)

if imagen is None:
    print("Error: no se pudo cargar la imagen. Verifica la ruta del archivo.")
else:
    # Obtener las dimensiones de la imagen original
    alto, ancho = imagen.shape[:2]

    # Redimensionar la imagen para el efecto pixel art
    factor_pixel_art = 0.1  # Ajusta este valor para mayor o menor detalle
    nueva_ancho = int(ancho * factor_pixel_art)
    nueva_alto = int(alto * factor_pixel_art)

    # Asegúrate de que la nueva dimensión sea al menos 1
    nueva_ancho = max(nueva_ancho, 1)
    nueva_alto = max(nueva_alto, 1)

    # Redimensionar usando INTER_NEAREST para el efecto pixel art
    imagen_reducida = cv2.resize(imagen, (nueva_ancho, nueva_alto), interpolation=cv2.INTER_NEAREST)

    # Redimensionar de nuevo a las dimensiones originales
    imagen_pixel_art = cv2.resize(imagen_reducida, (ancho, alto), interpolation=cv2.INTER_NEAREST)

    # Crear una ventana que se ajuste a la imagen pixel art
    cv2.namedWindow('Pixel Art', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Pixel Art', ancho, alto)

    # Mostrar la imagen en pixel art
    cv2.imshow('Pixel Art', imagen_pixel_art)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
