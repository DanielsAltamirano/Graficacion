# Image Processing with Grayscale and Convolution Filter

Este repositorio contiene un programa que aplica procesamiento de imágenes en **Python** y **OpenCV**. El programa carga una imagen, la convierte a escala de grises, la redimensiona, y finalmente aplica un filtro de suavizado mediante una **convolución**.

## Características
- Convierte una imagen a escala de grises.
- Redimensiona la imagen a la mitad de su tamaño original.
- Aplica un filtro de suavizado utilizando una matriz de convolución 3x3.
- Interfaz gráfica que muestra la imagen en varias etapas del procesamiento.

## Requisitos
- Python 3.x
- OpenCV
- Numpy

## Cómo ejecutar
1. Clona este repositorio o descarga el archivo.
2. Instala las dependencias necesarias ejecutando:
    ```bash
    pip install opencv-python numpy
    ```
3. Asegúrate de modificar la ruta de la imagen en el código (`ruta_imagen`) para que coincida con la ubicación de una imagen válida en tu sistema.
4. Ejecuta el programa:
    ```bash
    convolucion.py
    ```
   
   Se abrirán varias ventanas que muestran la imagen en diferentes etapas: original, en escala de grises, redimensionada, y con el filtro de suavizado aplicado.

## Personalización
- **Ruta de la imagen**: Cambia la variable `ruta_imagen` en el código para apuntar a la ubicación de la imagen que deseas procesar.
- **Matriz de convolución**: Puedes modificar la matriz 3x3 `matriz` en el código para aplicar diferentes tipos de filtros, como un filtro de bordes o un filtro de realce.

## Ejemplo de uso
### Imagen Original
![Imagen Original](https://raw.githubusercontent.com/DanielsAltamirano/Graficacion/refs/heads/master/Recursos/SharinganMadara.svg.png)

### Imagen en Escala de Grises
![Imagen Escala de Grises](https://raw.githubusercontent.com/DanielsAltamirano/Graficacion/refs/heads/master/Recursos/escala_grises.png)

### Imagen con Filtro de Suavizado
![Imagen Suavizada](https://raw.githubusercontent.com/DanielsAltamirano/Graficacion/refs/heads/master/Recursos/convolucion.png)

