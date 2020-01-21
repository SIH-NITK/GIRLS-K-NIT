import cv2
import os
import matplotlib
import numpy as np

def blur(image, kernel_size):
    kernel = np.ones((kernel_size,kernel_size),np.float32)/(kernel_size*kernel_size)
    blurred_image = cv2.filter2D(image,-1,kernel)
    return blurred_image