import cv2 as cv
import sys

cap = cv.VideoCapture(0, cv.CAP_DSHOW)

if not cap.isOpened():
    sys.exit("Could not open camera")

while True:
    ret, frame = cap.read()

    if not ret:
        print("Can't receive frame")
        break

    cv.imshow('Video display', frame)

    key = cv.waitKey(1)

    if key == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
