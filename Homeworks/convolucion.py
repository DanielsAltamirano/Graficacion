import cv2
import numpy as np

# Cargar la imagen
ruta_imagen = 'C:/Users/Daniels/Desktop/graficacion/Recursos/SharinganMadara.svg.png'  
imagen_original = cv2.imread(ruta_imagen)

# Convertir la imagen a escala de grises
imagen_gris = cv2.cvtColor(imagen_original, cv2.COLOR_BGR2GRAY)

# Escalar la imagen en escala de grises por un factor de 1/2
ancho, alto = imagen_gris.shape[1], imagen_gris.shape[0]
imagen_escalada = cv2.resize(imagen_gris, (ancho // 2, alto // 2), interpolation=cv2.INTER_LINEAR)

# Crear la matriz de convolución 3x3 para suavizado (todos los valores 1/9) 
matriz = np.ones((3, 3), np.float32) / 9

# Función para aplicar la convolución manualmente
def aplicar_convolucion(imagen, matriz):
    # Obtener dimensiones de la imagen y de la matriz
    h, w = imagen.shape
    k_h, k_w = matriz.shape
    
    # Calcular el padding necesario
    pad_h = k_h // 2
    pad_w = k_w // 2   
    
    # Crear una imagen con padding
    imagen_padded = np.pad(imagen, ((pad_h, pad_h), (pad_w, pad_w)), mode='edge')
    imagen_convolucionada = np.zeros_like(imagen)

    # Realizar la convolución
    for i in range(h):
        for j in range(w):
            # Extraer la región de interés
            region = imagen_padded[i:i + k_h, j:j + k_w]
            # Aplicar la matriz y almacenar el resultado
            imagen_convolucionada[i, j] = np.sum(region * matriz)
    
    return imagen_convolucionada

# Aplicar la convolución manualmente
imagen_convolucionada = aplicar_convolucion(imagen_escalada, matriz)

# Mostrar las imágenes
cv2.imshow("Imagen Original", imagen_original)
cv2.imshow("Imagen en Escala de Grises", imagen_gris)
cv2.imshow("Imagen Escalada 1/2", imagen_escalada)
cv2.imshow("Imagen Escalada con Filtro de Convolución", imagen_convolucionada)

# Esperar a que se cierre la ventana
cv2.waitKey(0)
cv2.destroyAllWindows()
