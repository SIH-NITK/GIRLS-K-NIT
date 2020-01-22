import cv2
import os
import matplotlib
import numpy as np

def change_contrast(image, contrast):
    if contrast != 0:
        f = 131*(contrast + 127)/(127*(131-contrast))
        alpha_c = f
        gamma_c = 127*(1-f)
        contrast_image = cv2.addWeighted(image, alpha_c, image, 0, gamma_c)

    return contrast_image