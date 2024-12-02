import glfw
from OpenGL.GL import *
from OpenGL.GLU import gluPerspective, gluLookAt, gluNewQuadric, gluCylinder, gluSphere
import sys

# Variables globales para la posición de la cámara
camera_x = 4.0
camera_y = 3.0
camera_z = 8.0
camera_speed = 0.5

def init():
    """Configuración inicial de OpenGL"""
    glClearColor(0.5, 0.8, 1.0, 1.0)  # Fondo azul cielo
    glEnable(GL_DEPTH_TEST)           # Activar prueba de profundidad

    # Configuración de la perspectiva
    glMatrixMode(GL_PROJECTION)
    gluPerspective(60, 1.0, 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

def draw_trunk():
    """Dibuja el tronco del árbol como un cilindro"""
    glPushMatrix()
    glColor3f(0.6, 0.3, 0.1)  # Marrón para el tronco
    glTranslatef(0.0, 0.0, 0.0)
    glRotatef(-90, 1, 0, 0)
    quadric = gluNewQuadric()
    gluCylinder(quadric, 0.3, 0.3, 2.0, 32, 32)
    glPopMatrix()

def draw_foliage():
    """Dibuja las hojas del árbol como una esfera"""
    glPushMatrix()
    glColor3f(0.1, 0.8, 0.1)  # Verde para las hojas
    glTranslatef(0.0, 2.0, 0.0)
    quadric = gluNewQuadric()
    gluSphere(quadric, 1.0, 32, 32)
    glPopMatrix()

def draw_ground():
    """Dibuja un plano para representar el suelo"""
    glBegin(GL_QUADS)
    glColor3f(0.3, 0.3, 0.3)  # Gris oscuro para el suelo
    glVertex3f(-10, 0, 10)
    glVertex3f(10, 0, 10)
    glVertex3f(10, 0, -10)
    glVertex3f(-10, 0, -10)
    glEnd()

def draw_scene():
    """Dibuja la escena completa con la posición de la cámara"""
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Configuración de la cámara
    gluLookAt(camera_x, camera_y, camera_z,  # Posición de la cámara
              0, 1, 0,                      # Punto al que mira
              0, 1, 0)                      # Vector hacia arriba

    draw_ground()  # Dibuja el suelo
    draw_trunk()   # Dibuja el tronco
    draw_foliage() # Dibuja las hojas

    glfw.swap_buffers(window)

def key_callback(window, key, scancode, action, mods):
    """Procesa las entradas de teclado para mover la cámara"""
    global camera_x, camera_y, camera_z, camera_speed

    if action == glfw.PRESS or action == glfw.REPEAT:
        if key == glfw.KEY_UP:    # Avanzar hacia adelante
            camera_z -= camera_speed
        elif key == glfw.KEY_DOWN:  # Retroceder
            camera_z += camera_speed
        elif key == glfw.KEY_LEFT:  # Moverse a la izquierda
            camera_x -= camera_speed
        elif key == glfw.KEY_RIGHT:  # Moverse a la derecha
            camera_x += camera_speed

def main():
    global window

    # Inicializar GLFW
    if not glfw.init():
        sys.exit()
    
    # Crear ventana de GLFW
    width, height = 800, 600
    window = glfw.create_window(width, height, "Escena 3D con Movimiento Libre", None, None)
    if not window:
        glfw.terminate()
        sys.exit()

    glfw.make_context_current(window)
    glfw.set_key_callback(window, key_callback)  # Configurar callback de teclado
    glViewport(0, 0, width, height)
    init()

    # Bucle principal
    while not glfw.window_should_close(window):
        draw_scene()
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()
