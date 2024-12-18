# Proyecto: Ciudad Interactiva en OpenGL

Este proyecto implementa una simulación interactiva utilizando **Python** y **OpenGL** que representa una ciudad en 3D. El programa incluye calles, edificios, casas, vehículos en movimiento, árboles, nieve, y objetos navideños como muñecos de nieve y regalos.

## Características Principales

- **Estructuras de la ciudad:** Calles, casas, edificios, parque y montañas.
- **Objetos en movimiento:** Vehículos (carros y camiones), Santa Claus con trineos, y copos de nieve que caen dinámicamente.
- **Elementos decorativos:** Árboles, cajas de regalo, muñecos de nieve y un parque central.
- **Interactividad:** Control de la cámara para explorar la ciudad.

## Tecnologías Utilizadas

- **Python**: Lenguaje de programación principal.
- **OpenGL**: Biblioteca para renderizado 3D.
- **GLFW**: Para la creación y administración de ventanas y entradas.
- **PyOpenGL**: Enlace de OpenGL para Python.
- **Random**: Para la generación de posiciones aleatorias.

## Requisitos Previos

1. Python 3.8 o superior.
2. Las siguientes librerías deben estar instaladas:
   ```bash
   pip install PyOpenGL glfw
   ```

## Cómo Ejecutar

1. Clona este repositorio o descarga los archivos fuente.
2. Abre una terminal en el directorio del proyecto.
3. Ejecuta el programa:
   ```bash
   python ciudad.py
   ```
4. Utiliza las teclas de flecha para mover la cámara:
   - **Flecha arriba:** Subir la cámara.
   - **Flecha abajo:** Bajar la cámara.
   - **Flecha izquierda:** Mover la cámara a la izquierda.
   - **Flecha derecha:** Mover la cámara a la derecha.
   - **W:** Acercar la cámara.
   - **S:** Alejar la cámara.

## Descripción del Código

### 1. Configuración Inicial
- Se inicializa OpenGL y GLFW para crear una ventana interactiva.
- Se configuran los parámetros de la cámara y la proyección.

### 2. Renderizado de Objetos
- **Calles y suelo:** Dibujadas como cuadriláteros con texturas básicas.
- **Edificios y casas:** Modelados como cubos con colores diferenciados.
- **Parque:** Incluye árboles y un lago central.
- **Vehículos:** Carros y camiones en movimiento.
- **Santa Claus:** Un modelo animado que se desplaza con sus trineos.

### 3. Elementos Dinámicos
- **Nieve:** Copos de nieve generados aleatoriamente que caen continuamente.
- **Vehículos:** Se mueven dentro de los límites de la ciudad y cambian de dirección.

### 4. Interacción
El programa incluye un sistema de cámara controlada por una malla mediante la deteccion de movimiento con flujo optico, lo que permite explorar la ciudad desde diferentes ángulos.

### 5. Optimización
- Se utilizan listas para almacenar posiciones de objetos como nieve y piedras.
- Los movimientos de los vehículos y Santa Claus están actualizados dinámicamente.

## Capturas de Pantalla


## Créditos

Proyecto desarrollado por: **[Altamirano Ramírez Daniels y Equipo]**

- **Asignatura:** Gráficación
- **Institución:** [Instituto tecnologico de morelia]

