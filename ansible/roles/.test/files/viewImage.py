import cv2 as cv

def readImage():
    img = cv.imread('cat.jpg')
    cv.imshow('cat', img)
    cv.waitKey(0)

readImage()
