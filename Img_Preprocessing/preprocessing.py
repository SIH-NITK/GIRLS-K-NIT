import noise
import blur
import normalize
import change_contrast
import resize
import cv2
import numpy as np
import read_images


images = read_images.load_images_from_folder("../Dataset")
contrast = 10
blur_kernel_size = 10
noise_kernel_size = 10
resize_factor = 0.60

def preprocessing():
    preprocessed = []
    for i in range(len(images)):
        temp = noise.denoise(images[i], noise_kernel_size)
        temp = blur.blur(temp, blur_kernel_size)
        temp = normalize.normalize(temp)
        temp = change_contrast.change_contrast(temp, contrast)
        height, width, channels = temp.shape
        temp = resize.resize(temp,int(height*resize_factor), int(width*resize_factor))
        #cv2.imshow("Preprocessed", temp)
        preprocessed.append(temp)
    preprocessed_array = np.array(preprocessed)
    print("Preprocessing done!", len(preprocessed), print(type(preprocessed_array)))
    return preprocessed_array

