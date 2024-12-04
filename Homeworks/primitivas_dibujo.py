import cv2
import numpy as np

width, height = 800, 600
image = np.zeros((height, width, 3), dtype=np.uint8)

# FIGURAS ARRIBA
# cuadrado
top_left_square = (50, 50)
side_length = 100
color = (255, 0, 0)  # Azul
# Dibujar un cuadrado en la imagen:
# - La esquina superior izquierda está en las coordenadas (top_left_square).
# - La esquina inferior derecha se calcula sumando el lado del cuadrado (side_length) a las coordenadas x e y.
# - El cuadrado se dibuja con el color especificado (en formato BGR) y está relleno porque el grosor es -1.
cv2.rectangle(image, top_left_square, (top_left_square[0] + side_length, top_left_square[1] + side_length), color, -1)

# rectángulo
top_left_rect = (200, 50)
color = (0, 255, 0)  # Verde
# Dibujar un rectángulo en la imagen:
# - La esquina superior izquierda está en las coordenadas (top_left_rect).
# - La esquina inferior derecha se calcula sumando 150 píxeles al eje x y 75 píxeles al eje y.
# - El rectángulo se dibuja con el color especificado (en formato BGR) y está relleno porque el grosor es -1.
cv2.rectangle(image, top_left_rect, (top_left_rect[0] + 150, top_left_rect[1] + 75), color, -1)

# triángulo
triangle_points = np.array([[400, 50], [350, 150], [450, 150]], np.int32)
triangle_points = triangle_points.reshape((-1, 1, 2))
color = (0, 0, 255)  # Rojo
# Dibujar un triángulo relleno en la imagen:
# - Se utiliza un conjunto de puntos definidos en triangle_points para crear el triángulo.
# - Los puntos deben estar organizados en un array NumPy con formato específico.
# - El triángulo se rellena con el color especificado (en formato BGR) gracias a la función cv2.fillPoly.
cv2.fillPoly(image, [triangle_points], color)

# círculo
center = (600, 100)
radius = 50
color = (255, 255, 0)  # Amarillo
# Dibujar un círculo relleno en la imagen:
# - El centro del círculo está en las coordenadas especificadas por center.
# - El radio del círculo está definido por radius.
# - Se usa el color especificado (en formato BGR).
# - El círculo está relleno porque el grosor es -1.
cv2.circle(image, center, radius, color, -1)

# FIGURAS ABAJO
# óvalo
center = (150, 400)
axes = (60, 40)
color = (255, 0, 255)  # Magenta
# Dibujar un óvalo (elipse) relleno en la imagen:
# - El centro del óvalo está definido por las coordenadas center.
# - Los ejes principales del óvalo (longitud del semieje mayor y menor) están dados por axes.
# - El ángulo de rotación del óvalo está configurado en 0 grados (sin rotación).
# - Se dibuja desde 0 hasta 360 grados, formando un óvalo completo.
# - Se utiliza el color especificado (en formato BGR).
# - El óvalo está relleno porque el grosor es -1.
cv2.ellipse(image, center, axes, 0, 0, 360, color, -1)

# diagonal
start_point = (300, 350)
end_point = (400, 450)
color = (0, 255, 255)  # Cian
thickness = 3
# Dibujar una línea en la imagen:
# - La línea comienza en las coordenadas especificadas por start_point.
# - Termina en las coordenadas especificadas por end_point.
# - El color de la línea se define en formato BGR.
# - El grosor de la línea se especifica con thickness.
cv2.line(image, start_point, end_point, color, thickness)

# estrella
star_points = np.array([[500, 350], [520, 400], [570, 400], [530, 430], [550, 480], [500, 450], [450, 480], [470, 430], [430, 400], [480, 400]], np.int32)
star_points = star_points.reshape((-1, 1, 2))
color = (0, 128, 255)  # Naranja
# Dibujar una estrella rellena en la imagen:
# - Los vértices de la estrella están definidos en star_points, que es un array NumPy con las coordenadas de los puntos.
# - Los puntos se pasan como una lista de arrays a la función cv2.fillPoly.
# - La estrella se rellena con el color especificado (en formato BGR).
cv2.fillPoly(image, [star_points], color)

# trapecio
trapecio_points = np.array([[650, 350], [750, 350], [700, 450], [680, 450]], np.int32)
trapecio_points = trapecio_points.reshape((-1, 1, 2))
color = (128, 255, 0)  # Verde claro
# Dibujar un trapecio relleno en la imagen:
# - Los vértices del trapecio están definidos en trapecio_points, que es un array NumPy con las coordenadas de los puntos.
# - Los puntos se pasan como una lista de arrays a la función cv2.fillPoly.
# - El trapecio se rellena con el color especificado (en formato BGR).
cv2.fillPoly(image, [trapecio_points], color)

#texto descriptivo
text = "Figuras Geometricas con OpenCV"
org = (200, 550)
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
color = (255, 255, 255)  
thickness = 2
cv2.putText(image, text, org, font, font_scale, color, thickness, cv2.LINE_AA)

# Mostrar la imagen
cv2.imshow("Primitivas de Dibujo", image)
cv2.waitKey(0)
cv2.destroyAllWindows()