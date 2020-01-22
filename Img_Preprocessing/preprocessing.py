import noise
import blur
import normalize
import change_contrast
import resize
import cv2
import numpy as np
import read_images
from PIL import Image

images = read_images.load_images_from_folder("../Dataset")
contrast = 10
blur_kernel_size = 10
noise_kernel_size = 10
resize_factor = 0.60

def load_images():
	images=[]
	for i in range(1,13,1):
		if i <=9:
		    st = "0"+ str(i)
		else:
		    st = str(i)
		img = cv2.imread('../Dataset/awifs_ndvi_2017'+st+'_15_1_clipped.tif')
		images.append(img)

	
	for i in range(1,13,1):
		if i <=9:
		    st = "0"+ str(i)
		else:
		    st = str(i)
		img = cv2.imread('../Dataset/awifs_ndvi_2018'+st+'_15_1_clipped.tif')
		images.append(img)
	return images

def preprocessing():
    images = load_images()
    preprocessed = []
    for i in range(len(images)):
        temp = images[i]#[:, :, 0]
        '''temp = noise.denoise(images[i], noise_kernel_size)
        temp = blur.blur(temp, blur_kernel_size)
        temp = normalize.normalize(temp)
        temp = change_contrast.change_contrast(temp, contrast)
        height, width, channels = temp.shape
        temp = resize.resize(temp,int(height*resize_factor), int(width*resize_factor))'''
        #cv2.imshow("Preprocessed", temp)	
        preprocessed.append(temp[:, :, 0])
    preprocessed_array = np.array(preprocessed)
    print("Preprocessing done!", len(preprocessed))
    return preprocessed_array

