import numpy as np
import cv2 as cv

# Cargar clasificadores para rostro y ojos
rostro = cv.CascadeClassifier(r'C:\Users\Daniels\Desktop\graficacion\Recursos\haarcascade_frontalface_alt.xml')
ojos = cv.CascadeClassifier(r'C:\Users\Daniels\Desktop\graficacion\Recursos\haarcascade_eye.xml')

# Cargar la imagen de corazón
heart_img = cv.imread(r'C:\Users\Daniels\Desktop\graficacion\Recursos\SharinganMadara.svg.png', -1)  # Imagen con canal alfa

# Función para superponer corazones
def overlay_image(background, overlay, x, y, w, h):
    overlay_resized = cv.resize(overlay, (w, h))  # Redimensionar el corazón al tamaño del ojo
    for i in range(overlay_resized.shape[0]):  # Altura de la imagen
        for j in range(overlay_resized.shape[1]):  # Anchura de la imagen
            if overlay_resized[i, j][3] != 0:  # Solo considerar píxeles que no sean transparentes
                background[y + i, x + j] = overlay_resized[i, j][:3]  # Copiar los valores de color BGR

# Iniciar la cámara
cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()
    # Voltear la imagen
    frame = cv.flip(frame, 1)

    # Convertir la imagen a escala de grises
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Detectar rostros
    rostros = rostro.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in rostros:
        # Dibujar un rectángulo alrededor del rostro
        frame = cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Obtener la región del rostro
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        # Detectar los ojos dentro del rostro
        ojos_detectados = ojos.detectMultiScale(roi_gray, 1.1, 18)

        # Colocar corazones sobre los ojos detectados
        for (ex, ey, ew, eh) in ojos_detectados:
            overlay_image(roi_color, heart_img, ex, ey, ew, eh)

    # Mostrar la imagen con los corazones
    cv.imshow('Rostros con corazones', frame)

    # Presionar 'Esc' para salir
    k = cv.waitKey(1)
    if k == 27:  # La tecla 'Esc'
        break

# Liberar la cámara y cerrar las ventanas
cap.release()
cv.destroyAllWindows()
