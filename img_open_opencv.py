#simple program to read and show an image
import cv2
#have a file names 'dog.jpg' in same directory
img=cv2.imread('dog.jpg')
cv2.imshow('Dog Image',img)

#waitKey(0) means wait till infinity. Ud have to close the window urself.
#if u put waitKey(1000) it'll wait 1000ms (1s) before it closes the imagw window.
cv2.waitKey(0)
cv2.destroyAllWindows()