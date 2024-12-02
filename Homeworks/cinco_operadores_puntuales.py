import cv2
import numpy as np

def apply_point_operators(image):
    # Convertimos la imagen a escala de grises si no lo está
    if len(image.shape) == 3:
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        gray_image = image

    # 1. Negativo de la imagen
    negative_image = 255 - gray_image

    # 2. Umbralización binaria
    _, binary_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

    # 3. Corrección gamma (gamma=2.0)
    gamma = 2.0
    gamma_corrected = np.array(255 * (gray_image / 255) ** gamma, dtype='uint8')

    # 4. Escala logarítmica
    log_image = np.array(255 * (np.log1p(gray_image) / np.log1p(255)), dtype='uint8')

    # 5. Escala exponencial
    exp_image = np.array(255 * (np.expm1(gray_image / 255) / np.expm1(1)), dtype='uint8')

    # Mostramos cada transformación en una ventana independiente
    cv2.imshow("Original", gray_image)
    cv2.imshow("Negativo", negative_image)
    cv2.imshow("Umbralización binaria", binary_image)
    cv2.imshow("Corrección Gamma (2.0)", gamma_corrected)
    cv2.imshow("Escala Logarítmica", log_image)
    cv2.imshow("Escala Exponencial", exp_image)

    # Espera a que se presione una tecla para cerrar todas las ventanas
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Cargar la imagen generada previamente o una cargada por el usuario
    image_path = "C:/Users/Daniels/Desktop/graficacion/Recursos/hongomario.jpg"  # Cambiar por la ruta de la imagen si es necesario
    image = cv2.imread(image_path)

    if image is not None:
        apply_point_operators(image)
    else:
        print("Error al cargar la imagen. Asegúrate de que la ruta es correcta.")
