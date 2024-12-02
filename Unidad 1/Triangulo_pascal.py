import cv2
import numpy as np

def pascal_triangle(n):
    """
    Genera el triángulo de Pascal hasta la fila n.
    :param n: Número de filas del triángulo
    :return: Lista con las filas del triángulo de Pascal
    """
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)
    return triangle

def draw_triangle(triangle):
    """
    Dibuja el triángulo de Pascal utilizando OpenCV.
    :param triangle: Lista con las filas del triángulo de Pascal
    """
    rows = len(triangle)
    img_height = rows * 50  # Espaciado vertical entre filas
    img_width = rows * 80   # Ajuste para ancho del triángulo
    img = np.zeros((img_height, img_width, 3), dtype=np.uint8)

    center_x = img_width // 2
    y_offset = 30  # Separación vertical inicial

    for i, row in enumerate(triangle):
        # Ajustar la posición inicial horizontal para centrar cada fila
        x_offset = center_x - (len(row) * 40 // 2)
        for j, value in enumerate(row):
            x = x_offset + j * 40  # Separación horizontal 
            y = y_offset + i * 50  # Separación vertical 
            cv2.circle(img, (x, y), 20, (255, 255, 255), -1)  # Dibuja el círculo
            cv2.putText(img, str(value), (x - 10, y + 5), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 1, cv2.LINE_AA)  # Dibuja el texto

    return img

if __name__ == "__main__":
    try:
        rows = int(input("Ingrese el número de filas para el Triángulo de Pascal: "))
        if rows <= 0:
            print("Por favor, ingrese un número positivo.")
        else:
            triangle = pascal_triangle(rows)
            triangle_image = draw_triangle(triangle)
            cv2.imshow("Triángulo de Pascal", triangle_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
    except ValueError:
        print("Por favor, ingrese un número válido.")
