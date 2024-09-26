import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

while(True):
    ret, img = cap.read()
    if ret:
        cv.imshow('video', img)
        hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
        
        # Define the upper and lower bounds for the HSV mask
        uba = (90, 255, 255)
        ubb = (40, 40, 40)
        
        # Create a mask using the defined bounds
        mask = cv.inRange(hsv, ubb, uba)
        res = cv.bitwise_and(img, img, mask=mask)
        
        # Show the result with the mask applied
        cv.imshow('res', res)

        # Wait for the 'ESC' key to exit
        k = cv.waitKey(1) & 0xFF
        if k == 27:  # 27 is the ESC key
            break
    else:
        break

# Release the capture and close all windows
cap.release()
cv.destroyAllWindows()
