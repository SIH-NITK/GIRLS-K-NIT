import cv2 as cv
import numpy as np

def normalize(img):

	normalizedImg = np.zeros((2118, 2135))
	normalizedImg = cv.normalize(img,  normalizedImg, 0, 255, cv.NORM_MINMAX)
	return normalizedImg


