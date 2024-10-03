import cv2
import numpy as np
import random

# Definir colores iniciales
BLACK = (0, 0, 0)


# Dimensiones de la ventana
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Propiedades del "logo" que se moverá
logo_width, logo_height = 150, 80
logo_x, logo_y = 200, 150
logo_speed_x, logo_speed_y = 10, 10  # Velocidad del logo

# Generar un color aleatorio
def get_random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Crear una función para dibujar texto en la pantalla
def draw_text(image, text, position, font=cv2.FONT_HERSHEY_SIMPLEX, font_scale=1, color=(255, 255, 255), thickness=2):
    cv2.putText(image, text, position, font, font_scale, color, thickness, lineType=cv2.LINE_AA)

# Función principal de la animación
def main():
    global logo_x, logo_y, logo_speed_x, logo_speed_y

    # Color inicial del logo
    logo_color = get_random_color()

    while True:
        # Crear una imagen negra (el fondo)
        screen = np.zeros((SCREEN_HEIGHT, SCREEN_WIDTH, 3), dtype=np.uint8)

        # Mover el "logo"
        logo_x += logo_speed_x
        logo_y += logo_speed_y

        # Detectar colisiones con los bordes y hacer que rebote
        if logo_x <= 0 or logo_x + logo_width >= SCREEN_WIDTH:
            logo_speed_x = -logo_speed_x  # Rebote en los bordes laterales
            logo_color = get_random_color()  # Cambiar el color al colisionar

        if logo_y <= 0 or logo_y + logo_height >= SCREEN_HEIGHT:
            logo_speed_y = -logo_speed_y  # Rebote en los bordes superiores e inferiores
            logo_color = get_random_color()  # Cambiar el color al colisionar

        # Dibujar el "logo" (un elipse con letras dentro)
        cv2.ellipse(screen, (logo_x + logo_width // 2, logo_y + logo_height // 2), 
                    (logo_width // 2, logo_height // 2), 0, 0, 360, logo_color, -1)

        # Dibujar texto dentro del logo (centrado)
        text = "DVD"  # Texto dentro del logo
        text_size = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 1, 2)[0]
        text_x = logo_x + (logo_width - text_size[0]) // 2
        text_y = logo_y + (logo_height + text_size[1]) // 2
        cv2.putText(screen, text, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

        # Añadir texto en la pantalla
        draw_text(screen, "Daniels Altamirano", (20, 50))

        # Mostrar la imagen resultante
        cv2.imshow('DVD Bounce Simulation', screen)

        # Controlar la velocidad de actualización (60 FPS aprox.)
        if cv2.waitKey(16) & 0xFF == ord('q'):  # Salir si presionas 'q'
            break

    # Liberar los recursos al finalizar
    cv2.destroyAllWindows()

# Ejecutar el programa
if __name__ == "__main__":
    main()
