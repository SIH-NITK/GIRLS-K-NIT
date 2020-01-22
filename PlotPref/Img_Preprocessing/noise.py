import cv2
import os
import matplotlib
import numpy as np

def denoise(image, kernel_size):
    median = cv2.medianBlur(image,5)
    return median