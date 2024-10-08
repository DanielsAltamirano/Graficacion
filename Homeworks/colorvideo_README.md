# Detección de Colores en Video en Tiempo Real

Este proyecto contiene un script en **Python** que captura video desde la cámara de la laptop y detecta los colores **rojo**, **verde** y **amarillo** en tiempo real. Utiliza **OpenCV** para procesar el video cuadro por cuadro, aplicando filtros de color mediante el modelo de color HSV.

## Características
- Captura video en tiempo real desde la cámara de la laptop.
- Convierte cada cuadro del video de BGR a HSV para facilitar la detección de colores.
- Detecta y resalta los colores **rojo**, **verde** y **amarillo** utilizando máscaras.
- Muestra el video original junto con las versiones filtradas para cada color.

## Requisitos
- Python 3.x
- OpenCV
- Numpy

## Instalación y ejecución
1. **Clona este repositorio:**
2. **Instala las dependencias necesarias:**

    ```bash
    pip install opencv-python numpy
    ```
3. **Ejecuta el script:**
    ```bash
    python colorvideo.py
    ```
4. Presiona `q` para salir del programa y cerrar todas las ventanas.
----
