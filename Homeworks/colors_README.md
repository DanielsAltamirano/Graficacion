# Detección de Colores en una Imagen usando OpenCV

Este repositorio contiene un script en **Python** que permite detectar y resaltar colores específicos (**rojo**, **verde** y **amarillo**) en una imagen utilizando **OpenCV** y **Numpy**. El programa carga una imagen, la convierte al espacio de color HSV, crea máscaras para cada color definido y muestra la imagen original junto con las imágenes filtradas de cada color detectado.

## Características
- Carga y muestra una imagen desde una ruta especificada.
- Convierte la imagen del espacio de color BGR a HSV.
- Define rangos de colores en HSV para detectar **rojo**, **verde** y **amarillo**.
- Crea máscaras para cada color y aplica estas máscaras a la imagen original.
- Muestra la imagen original y las imágenes filtradas correspondientes a cada color detectado.

## Requisitos
- Python 3.x
- OpenCV
- Numpy

## Instalación
1. **Clona este repositorio:**
2. **Instala las dependencias necesarias:**
    ```bash
    pip install opencv-python numpy
    ```

## Cómo ejecutar
1. **Asegúrate de tener una imagen para procesar y actualiza la ruta de la imagen en el codigo si es necesario:**
    ```python
    ruta_imagen = r'C:\Users\Desktop\manzanascolors.jpg'
    ```
2. **Ejecuta el codigo:**
    ```bash
    python colors.py
    ```
3. **El programa mostrará la imagen original y las imágenes filtradas de cada color. Presiona cualquier tecla en una de las ventanas de imagen para cerrar todas las ventanas.**
------

