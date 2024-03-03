import cv2 as cv
import sys

img = cv.imread('girl_laughing.jpg')

if img is None:
    sys.exit('Could not load image')


def paint(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(img, (x,y), 5, (255, 0, 0), -1)
    elif event == cv.EVENT_MOUSEMOVE and flags & cv.EVENT_FLAG_LBUTTON:
        cv.circle(img, (x, y), 5, (255, 0, 0), -1)
    elif event == cv.EVENT_RBUTTONDOWN:
        cv.rectangle(img, (x, y), (x + 100, y + 100), (255, 0, 0), 2)

    cv.imshow('Painting', img)


cv.namedWindow('Painting')
cv.imshow('Painting', img)

# 마우스 콜백 함수 지정
cv.setMouseCallback('Painting', paint)

while True:
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break
