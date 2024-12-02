# Operadores Puntuales de Imágenes

Este repositorio contiene un programa que aplica diversos operadores puntuales a una imagen utilizando **Python**, **OpenCV**, y **NumPy**. El programa transforma la imagen original en escala de grises y realiza operaciones como el negativo, umbralización binaria, corrección gamma, escalas logarítmica y exponencial.

## Características
- Conversión automática de imágenes a escala de grises (si no lo están).
- Aplicación de los siguientes operadores puntuales:
  1. Negativo de la imagen.
  2. Umbralización binaria.
  3. Corrección Gamma (γ = 2.0).
  4. Transformación a escala logarítmica.
  5. Transformación a escala exponencial.
- Visualización de las imágenes procesadas en ventanas separadas.

## Requisitos
- Python 3.x
- OpenCV
- NumPy

## Cómo ejecutar
1. Clona este repositorio.
2. Instala las dependencias:
    ```bash
    pip install opencv-python-headless numpy
    ```
3. Asegúrate de proporcionar una ruta válida a la imagen en el código:
4. Ejecuta el programa:
    ```bash
    python cinco_operadores_puntuales.py
    ```

## Salida esperada
Al ejecutar el programa, se abrirán ventanas mostrando las siguientes transformaciones de la imagen:
- **Original**: Imagen en escala de grises.
- **Negativo**: Imagen invertida.
- **Umbralización binaria**: Imagen binarizada.
- **Corrección Gamma (2.0)**: Imagen ajustada con corrección gamma.
- **Escala Logarítmica**: Imagen transformada logarítmicamente.
- **Escala Exponencial**: Imagen transformada exponencialmente.

Presiona cualquier tecla en las ventanas para cerrarlas.

---

## Nota
Si el programa no puede cargar la imagen, asegúrate de que la ruta especificada en `image_path` sea correcta y que el archivo exista en dicha ubicación.
