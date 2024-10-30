# Face and Eye Sharingan Overlay

Este repositorio contiene un programa que detecta **rostros y ojos** en tiempo real utilizando **Python** y **OpenCV** y superpone una imagen de **Sharingan** sobre los ojos detectados, generando un efecto visual en tiempo real.

## Características
- Detecta rostros y ojos en una transmisión de video en tiempo real.
- Superpone una imagen de Sharingan sobre los ojos detectados.
- Efecto visual en tiempo real con ajustes de tamaño para adaptarse a cada detección de ojos.

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
3. Asegúrate de modificar las rutas de los archivos de los clasificadores y de la imagen de Sharingan en el código para que coincidan con la ubicación en tu sistema.
4. Ejecuta el programa:
    ```bash
    deteccion_de_rostro_ojos.py
    ```
   
   Se abrirá una ventana de video en la que podrás ver el efecto de Sharingan aplicado en tus ojos en tiempo real.

## Personalización
- **Ruta de los clasificadores**: Asegúrate de que las rutas para los clasificadores de rostro y ojos (`haarcascade_frontalface_alt.xml` y `haarcascade_eye.xml`) apunten a la ubicación correcta en tu sistema.
- **Imagen superpuesta**: Edita la ruta de `heart_img` en el código para utilizar una imagen diferente (en este caso, una imagen de Sharingan). La imagen debe tener un canal alfa (transparencia) para un mejor resultado.
- **Tamaño de superposición**: La función `overlay_image()` ajusta el tamaño de la imagen superpuesta en función de las dimensiones de los ojos detectados para un efecto más realista.

## Ejemplo de uso
### Detección sin superposición  
![Rostro detectado sin efecto](https://raw.githubusercontent.com/DanielsAltamirano/Graficacion/refs/heads/master/Recursos/Sinfiltro.png)

### Detección con superposición de Sharingan
![Rostro detectado con Sharingan en los ojos](https://raw.githubusercontent.com/DanielsAltamirano/Graficacion/refs/heads/master/Recursos/Confiltro.png)

