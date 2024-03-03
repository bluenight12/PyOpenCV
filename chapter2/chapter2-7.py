import cv2 as cv
import sys

img = cv.imread('girl_laughing.jpg')

if img is None:
    sys.exit('Could not load image')


def draw(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        cv.rectangle(img, (x, y), (x + 200, y + 200), (0, 0, 255), 2)
    elif event == cv.EVENT_RBUTTONDOWN:
        cv.rectangle(img, (x, y), (x + 100, y + 100), (255, 0, 0), 2)

    cv.imshow('Drawing', img)


cv.namedWindow('Drawing')
cv.imshow('Drawing', img)

# 마우스 콜백 함수 지정
cv.setMouseCallback('Drawing', draw)

while True:
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break
