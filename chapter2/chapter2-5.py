import cv2 as cv
import numpy as np
import sys

cap = cv.VideoCapture(0, cv.CAP_DSHOW)

frames = []

if not cap.isOpened():
    sys.exit("Could not open camera")

while True:
    ret, frame = cap.read()

    if not ret:
        print("Can't receive frame")
        break

    cv.imshow('Video display', frame)

    key = cv.waitKey(1)
    if key == ord('c'):
        frames.append(frame)

    if key == ord('q'):
        break

cap.release()
cv.destroyAllWindows()

if len(frames) > 0:
    imgs = frames[0]
    for i in range(1, min(3,len(frames))):
        imgs = np.hstack((imgs, frames[i]))

    cv.imshow('collected images', imgs)

    cv.waitKey()
    cv.destroyAllWindows()