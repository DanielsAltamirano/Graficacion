# Primitivas de Dibujo con OpenCV

Este repositorio contiene un programa en **Python** que utiliza **OpenCV** y **NumPy** para dibujar varias figuras geométricas en una imagen. Las figuras se disponen de forma estética en una ventana para su visualización.

## Características
- Dibuja varias figuras geométricas: cuadrado, rectángulo, triángulo, círculo, óvalo, línea diagonal, estrella y trapecio.
- Las figuras se dibujan con colores diferentes y se encuentran organizadas de manera estética en la imagen.
- Se incluye un texto descriptivo de las figuras en la parte inferior de la imagen.

## Requisitos
- Python 3.x
- OpenCV
- NumPy

## Cómo ejecutar
1. Clona este repositorio.
2. Instala las dependencias:
    ```bash
    pip install opencv-python numpy
    ```
3. Ejecuta el programa:
    ```bash
    python primitivas_dibujo.py
    ```

## Explicación del Código
El código genera una imagen con las siguientes figuras:
- **Cuadrado**: Se dibuja en la parte superior izquierda con color azul.
- **Rectángulo**: Se dibuja a la derecha del cuadrado con color verde.
- **Triángulo**: Se dibuja en la parte superior central con color rojo.
- **Círculo**: Se dibuja en la parte superior derecha con color amarillo.
- **Óvalo**: Se dibuja en la parte inferior izquierda con color magenta.
- **Línea Diagonal**: Se dibuja en la parte inferior central con color cian.
- **Estrella**: Se dibuja en la parte inferior central con color naranja.
- **Trapecio**: Se dibuja en la parte inferior derecha con color verde claro.

Todas las figuras están rellenas con los colores especificados.

## Salida esperada
Al ejecutar el programa, se abrirá una ventana mostrando la imagen con las figuras geométricas dibujadas y el texto descriptivo en la parte inferior de la ventana.

![Salida Esperada](https://raw.githubusercontent.com/DanielsAltamirano/Graficacion/refs/heads/master/Recursos/primitivas_dibujo.png)

Presiona cualquier tecla en la ventana para cerrarla.

## Nota
Si el programa no puede mostrar la ventana, asegúrate de tener instalada correctamente la librería OpenCV y que no haya errores en el código.
