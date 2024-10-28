# Pixel Art
Este repositorio contiene un programa que aplica un efecto de **Pixel Art** a una imagen utilizando **Python** y **OpenCV**. El programa redimensiona una imagen y luego la vuelve a escalar para crear un estilo visual **"pixelado"** , similar al arte de videojuegos retro.

## Características
- Aplica un efecto de Pixel Art a cualquier imagen.
- Permite ajustar el nivel de pixelado mediante el valor del factor de reducción.
- Interfaz gráfica que muestra la imagen en una ventana redimensionable.

## Requisitos
- Python 3.x
- OpenCV
- Numpy

## Cómo ejecutar
1. Clona este repositorio o descarga el archivo.
2. Instala las dependencias necesarias ejecutando el siguiente comando:
    ```bash
    pip install opencv-python numpy
    ```
3. Asegúrate de modificar la ruta de la imagen en el código para que apunte a una imagen válida en tu sistema.
4. Ejecuta el programa:
    ```bash
    python pixel_art.py
    ```

El programa abrirá una ventana mostrando la imagen con el efecto de Pixel Art aplicado.

## Personalización
- **Ruta de la imagen**: Edita la variable `ruta_imagen` en el código para que apunte a la ubicación de la imagen que desees procesar.
- **Factor de Pixel Art**: Modifica la variable `factor_pixel_art` para ajustar el nivel de pixelado. Valores más bajos incrementan el nivel de pixelado y valores más altos lo reducen.

## Ejemplo
### Imagen Original 
![Pixel Art Example](https://raw.githubusercontent.com/DanielsAltamirano/Graficacion/refs/heads/master/Recursos/SharinganMadara.svg.png)
### Imagen Pixelada
![Pixel Art Example](https://github.com/DanielsAltamirano/Graficacion/blob/master/Recursos/PixelArt.png?raw=true)
