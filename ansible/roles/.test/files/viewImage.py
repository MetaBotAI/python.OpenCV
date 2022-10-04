import cv2 as cv

def readImage():
    img = cv.imread('cat.jpeg')
    cv.imshow('cat', img)
    cv.waitKey(0)

readImage

cv.waitKey(0)
