import cv2 as cv

cap = cv.VideoCapture(0)  # Captura de video desde la cámara principal

while(True):
    ret, img = cap.read()  # Lee un frame del video
    if ret:  # Si la captura es exitosa
        cv.imshow('video', img)  # Muestra el frame en una ventana llamada 'video'
        
        img2 =cv.cvtColor(img, cv.COLOR_BGR2RGB)
        cv.imshow('video2', img2)
        k = cv.waitKey(1) & 0xFF  # Espera por una tecla y obtiene su valor en ASCII
        if k == 27:  # Si la tecla presionada es 'ESC' (código 27)
            break  # Sale del bucle
    else:
        break  # Si la captura no es exitosa, sale del bucle

cap.release()  # Libera la captura de video
cv.destroyAllWindows()  # Cierra todas las ventanas creadas por OpenCV
