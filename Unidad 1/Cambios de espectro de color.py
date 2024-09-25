import cv2 as cv  # Importar OpenCV
import numpy as np  # Importar NumPy para operaciones matriciales

# Leer la imagen a color desde la ruta especificada
img = cv.imread(r'C:\Users\Daniels\Downloads\hongomario.jpg')
# Mostrar la imagen original en una ventana
cv.imshow('Imagen Original', img)

# Obtener las dimensiones de la imagen (ancho, alto, número de canales)
x, y, z = img.shape

# Separar los tres canales de color (B, G, R) de la imagen
channels = cv.split(img)

# Listas vacías para almacenar los resultados de los operadores aplicados a cada canal
negativo_channels = []
umbral_channels = []
contraste_channels = []

# Parámetros para los operadores
umbral_val = 128  # Valor del umbral para el operador umbral
factor_contraste = 1.5  # Factor de aumento de contraste
ajuste_contraste = -50  # Ajuste para el operador de contraste

# Aplicar los operadores a cada canal de la imagen (B, G, R)
for channel in channels:
    # Operador Negativo: 255 menos el valor de cada pixel del canal
    negativo_channels.append(255 - channel)
    
    # Operador Umbral: Si el pixel es mayor o igual al umbral, se asigna 255, si no, 0
    _, umbral_channel = cv.threshold(channel, umbral_val, 255, cv.THRESH_BINARY)
    umbral_channels.append(umbral_channel)
    
    # Operador Contraste: Ajustar el contraste y limitar los valores entre 0 y 255
    contraste_channel = np.clip(factor_contraste * channel + ajuste_contraste, 0, 255).astype(np.uint8)
    contraste_channels.append(contraste_channel)

# Combinar los resultados de los canales de nuevo en una imagen BGR
negativo = cv.merge(negativo_channels)
umbral = cv.merge(umbral_channels)
contraste = cv.merge(contraste_channels)

# Mostrar las imágenes resultantes en ventanas separadas
cv.imshow('Negativo', negativo)
cv.imshow('Umbral', umbral)
cv.imshow('Contraste Aumentado', contraste)

# Imprimir las dimensiones de la imagen original
print(f'Dimensiones: {img.shape}, {x} {y} {z}')

# Esperar hasta que se presione una tecla y luego cerrar todas las ventanas
cv.waitKey(0)
cv.destroyAllWindows()
