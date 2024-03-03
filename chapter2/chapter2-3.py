import cv2 as cv
import sys

img = cv.imread('ori.png')

if img is None:
    sys.exit('Could not load image')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray_small = cv.resize(gray, dsize=(0, 0), fx=0.5, fy=0.5)

cv.imwrite('ori_gray.png', gray)
cv.imwrite('ori_gray_small.png', gray_small)

cv.imshow('Color image', img)
cv.imshow('Gray image', gray)
cv.imshow('Gray image small', gray_small)

cv.waitKey()
cv.destroyAllWindows()
