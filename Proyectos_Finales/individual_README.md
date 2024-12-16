# Proyecto final [Movimientos de rotación,traslación y escalimeinto en un objeto]

Este proyecto implementa un programa interactivo que utiliza **Python**, **OpenCV**, y **Mediapipe** para detectar manos y controlar la posición, tamaño y rotación de una bola en pantalla en tiempo real. El código está cuidadosamente comentado, lo que facilita su comprensión.

## Características

- Detección de manos en tiempo real utilizando la librería Mediapipe.
- Seguimiento de la posición de la palma de la mano para mover la bola.
- Ajuste dinámico del tamaño de la bola basado en la distancia entre los dedos índice y medio.
- Rotación de la bola basada en la distancia entre dos puntos de referencia.
- Interfaz visual que combina el video capturado con los elementos gráficos generados.

## Tecnologías Utilizadas

- **Python**: Lenguaje de programación principal.
- **OpenCV**: Procesamiento de imágenes y video.
- **Mediapipe**: Detección y seguimiento de manos.
- **NumPy**: Manipulación de arrays y cálculos matemáticos.

## Librerías Principales

1. **OpenCV**: Permite capturar video en tiempo real y dibujar elementos como círculos y matrices de rotación sobre los cuadros capturados.
2. **Mediapipe**: Proporciona soluciones de aprendizaje automático para la detección y el seguimiento de manos.
3. **NumPy**: Se utiliza para realizar cálculos matemáticos como distancias entre puntos y manipular arrays de coordenadas.

## Cómo Ejecutar

1. Asegúrate de tener **Python 3.8** o superior instalado.
2. Instala las dependencias necesarias ejecutando:
   ```bash
   pip install opencv-python mediapipe numpy
   ```
3. Ejecuta el programa:
   ```bash
   python individial.py
   ```
4. Presiona `ESC` para salir del programa.

## Estructura del Código

### 1. Importación de Librerías

El programa importa las librerías necesarias para la detección de manos, el procesamiento de video y las operaciones matemáticas.

```python
import numpy as np
import cv2 as cv
import mediapipe as mp
```

### 2. Inicialización de Mediapipe y Captura de Video

- Se inicializan los módulos de Mediapipe para la detección de manos con una confianza mínima configurada al 70%.
- Se configura la captura de video desde la cámara predeterminada.

```python
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
cap = cv.VideoCapture(0)
```

### 3. Detección de Puntos Clave de las Manos

El programa detecta las manos y extrae tres puntos clave:

- Punta del dedo índice.
- Punta del dedo medio.
- Base de la palma (muñeca).
  Estas coordenadas se utilizan para:
- Mover la bola a la posición de la palma.
- Ajustar el radio de la bola basado en la distancia entre el índice y el medio.
- Calcular ángulos de rotación según la distancia entre dos puntos de referencia.

### 4. Dibujar y Transformar la Bola

- La bola se dibuja como un círculo verde.
- Se calcula una matriz de rotación para aplicarla a la bola.
- Se combinan los cuadros originales con los gráficos generados.

```python
rotation_matrix = cv.getRotationMatrix2D(rotation_center, rotation_angle, 1)
rotated_ball = cv.warpAffine(rotated_ball, rotation_matrix, (frame_width, frame_height))
```

### 5. Mostrar el Video Procesado

El video procesado se muestra en tiempo real, junto con la bola interactiva y los puntos de referencia.

```python
cv.imshow('Control de Bola', frame)
```

### 6. Liberar Recursos

Se liberan los recursos de la cámara y se cierran todas las ventanas al presionar `ESC`.

## Resultados Esperados

- **Interacción en Tiempo Real**: Una bola verde sigue la posición de la palma de la mano.
- **Tamaño Dinámico**: El radio de la bola cambia según la distancia entre los dedos índice y medio.
- **Rotación Interactiva**: La bola rota dependiendo de la distancia entre dos puntos rojos.

## Capturas de Pantalla



- Asegúrate de trabajar en un entorno bien iluminado para mejorar la detección de las manos.
- Puedes ajustar los parámetros de detección y seguimiento en el módulo de Mediapipe para obtener mejores resultados en diferentes condiciones.
#

# Autor
 **[Daniels John Altamirano Ramírez]** - Proyecto Final de Graficación en Ingeniería Sistemas Computacionales.

