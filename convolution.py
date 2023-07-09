import cv2 as cv 
import numpy as np

image = cv.imread("./french_kawpun.jpg", cv.IMREAD_GRAYSCALE)
kernell = cv.imread("./line_of_result.png", cv.IMREAD_GRAYSCALE)

n = kernell.sum()
kernell = kernell/n

image = cv.filter2D(src = image, ddepth= -1, kernel= kernell)
cv.imwrite("./result_of_combine2.png", image)