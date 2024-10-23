import cv2
import numpy as np

# Función para mostrar un menú simple y seleccionar un filtro
def seleccionar_filtro():
    print("Selecciona un filtro:")
    print("1. Máscara de Tobi")
    print("2. Máscara de Orus")
    print("3. Máscara de gas")
    print("4. Lentes")
    opcion = input("Ingresa el número del filtro que deseas aplicar: ")
    return opcion

# Función para cargar la máscara según la opción seleccionada
def cargar_mascara(opcion):
    if opcion == '1':
        return cv2.imread(r'C:\Users\Daniels\Desktop\graficacion\Recursos\tobimascara.png', cv2.IMREAD_UNCHANGED)
    elif opcion == '2':
        return cv2.imread(r'C:\Users\Daniels\Desktop\graficacion\Recursos\orus.png', cv2.IMREAD_UNCHANGED)
    elif opcion == '3':
        return cv2.imread(r'C:\Users\Daniels\Desktop\graficacion\Recursos\mascara_gas.png', cv2.IMREAD_UNCHANGED)
    elif opcion == '4':
        return cv2.imread(r'C:\Users\Daniels\Desktop\graficacion\Recursos\lentes.png', cv2.IMREAD_UNCHANGED)
    else:
        print("Opción no válida. Usando la máscara de Tobi por defecto.")
        return cv2.imread(r'C:\Users\Daniels\Desktop\graficacion\Recursos\tobimascara.png', cv2.IMREAD_UNCHANGED)

# Cargar los clasificadores preentrenados de rostros y ojos
face_cascade = cv2.CascadeClassifier(r'C:\Users\Daniels\Desktop\graficacion\Recursos\haarcascade_frontalface_alt.xml')
eye_cascade = cv2.CascadeClassifier(r'C:\Users\Daniels\Desktop\graficacion\Recursos\haarcascade_eye.xml')

# Capturar video desde la cámara
video = cv2.VideoCapture(0)

# Seleccionar el primer filtro
opcion_filtro = seleccionar_filtro()
mascara = cargar_mascara(opcion_filtro)

# Verificar si la máscara tiene canal alfa
if mascara.shape[2] != 4:
    print("Error: La máscara seleccionada no tiene canal alfa.")
    exit()

while True:
    # Leer cada frame del video
    ret, frame = video.read()

    if not ret:
        break

    # Corregir la imagen invertida
    frame = cv2.flip(frame, 1)

    # Convertir el frame a escala de grises
    frame_gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectar los rostros en el frame
    rostros = face_cascade.detectMultiScale(frame_gris, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Procesar cada rostro detectado
    for (x, y, w, h) in rostros:
        # Redimensionar la máscara para que coincida con el tamaño del rostro detectado
        mascara_redimensionada = cv2.resize(mascara, (w, h))

        # Separar los canales de la máscara: color y alfa (transparencia)
        mascara_rgb = mascara_redimensionada[:, :, :3]
        mascara_alpha = mascara_redimensionada[:, :, 3]

        # Asegurarse de que la máscara alfa sea de tipo uint8
        mascara_alpha = cv2.convertScaleAbs(mascara_alpha)

        # Si se seleccionan lentes, usar el detector de ojos
        if opcion_filtro == '4':
            # Detectar ojos dentro del rostro
            roi_gris = frame_gris[y:y+h, x:x+w]
            ojos = eye_cascade.detectMultiScale(roi_gris)

            # Aplicar lentes solo si se detectan dos ojos
            if len(ojos) == 2:
                # Obtener las coordenadas de los ojos
                (ex1, ey1, ew1, eh1) = ojos[0]
                (ex2, ey2, ew2, eh2) = ojos[1]

                # Calcular el centro entre los ojos y el ancho total
                ojo_centro_x = (ex1 + ex2 + ew1 + ew2) // 2
                ojo_centro_y = (ey1 + ey2) // 2
                ancho_total_ojos = ex2 + ew2 - ex1

                # Redimensionar los lentes según el tamaño de los ojos
                lentes_redimensionados = cv2.resize(mascara, (ancho_total_ojos, eh1))
                lentes_rgb = lentes_redimensionados[:, :, :3]
                lentes_alpha = lentes_redimensionados[:, :, 3]

                # Crear región de interés (ROI) para los lentes
                y_lentes = y + ey1 - eh1 // 2
                x_lentes = x + ex1 - ew1 // 2

                # Asegurar que los lentes estén dentro de los límites del rostro
                if y_lentes >= 0 and x_lentes >= 0:
                    roi_lentes = frame[y_lentes:y_lentes+eh1, x_lentes:x_lentes+ancho_total_ojos]

                    # Aplicar lentes con máscara alfa
                    mascara_alpha_inv = cv2.bitwise_not(lentes_alpha)
                    fondo = cv2.bitwise_and(roi_lentes, roi_lentes, mask=mascara_alpha_inv)
                    lentes_fg = cv2.bitwise_and(lentes_rgb, lentes_rgb, mask=lentes_alpha)
                    resultado_lentes = cv2.add(fondo, lentes_fg)
                    frame[y_lentes:y_lentes+eh1, x_lentes:x_lentes+ancho_total_ojos] = resultado_lentes
        else:
            # Crear una región de interés (ROI) en el frame donde colocaremos la máscara
            roi = frame[y:y+h, x:x+w]

            # Asegurarse de que la ROI y la máscara tengan el mismo tamaño
            if roi.shape[:2] == mascara_alpha.shape[:2]:
                # Invertir la máscara alfa para obtener la parte del rostro donde se aplicará la máscara
                mascara_alpha_inv = cv2.bitwise_not(mascara_alpha)

                # Enmascarar la región del rostro en la imagen original
                fondo = cv2.bitwise_and(roi, roi, mask=mascara_alpha_inv)

                # Enmascarar la máscara RGB
                mascara_fg = cv2.bitwise_and(mascara_rgb, mascara_rgb, mask=mascara_alpha)

                # Combinar el fondo (parte del rostro sin máscara) y la parte con la máscara
                resultado = cv2.add(fondo, mascara_fg)

                # Reemplazar la región del rostro con la imagen combinada
                frame[y:y+h, x:x+w] = resultado

    # Mostrar el frame con la máscara aplicada
    cv2.imshow('Video con filtro', frame)

    # Detectar las teclas presionadas
    key = cv2.waitKey(1) & 0xFF

    # Cambiar de filtro con 'c'
    if key == ord('c'):
        opcion_filtro = seleccionar_filtro()
        mascara = cargar_mascara(opcion_filtro)

        # Verificar si la nueva máscara tiene canal alfa
        if mascara.shape[2] != 4:
            print("Error: La nueva máscara no tiene canal alfa.")
            break

    # Cerrar con la tecla 'Esc'
    elif key == 27:  # Tecla 'Esc'
        break

# Liberar la captura de video y cerrar las ventanas
video.release()
cv2.destroyAllWindows()
