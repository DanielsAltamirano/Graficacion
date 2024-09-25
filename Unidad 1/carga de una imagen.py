import cv2 as cv
img = cv.imread(r'C:\Users\Daniels\Downloads\hongomario.jpg')
cv.imshow('ejemplo',img)
cv.waitKey(0)
cv.destroyAllWindows()