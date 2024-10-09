import cv2 as cv
img = cv.imread(r'C:\Users\Daniels\Desktop\graficacion\Recursos\hongomario.jpg')
cv.imshow('ejemplo',img)
cv.waitKey(0)
cv.destroyAllWindows()