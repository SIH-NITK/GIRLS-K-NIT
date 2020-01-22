import noise
import blur
import normalize
import change_contrast
import resize
import cv2
import numpy as np
import read_images
from PIL import Image

#images = read_images.load_images_from_folder("../Dataset")
contrast = 10
blur_kernel_size = 10
noise_kernel_size = 10
resize_factor = 0.60

def load_images():
	ar = np.zeros((24,2118,2135))
	for i in range(1,13,1):
		if i <=9:
		    st = "0"+ str(i)
		else:
		    st = str(i)
		img = Image.open('../Dataset/awifs_ndvi_2017'+st+'_15_1_clipped.tif')
		img.seek(0)
		for x in range(0,2118):
		    for y in range(0,2135):
		        ar[i-1][x][y] = img.getpixel((x, y))
	for i in range(1,13,1):
		if i <=9:
		    st = "0"+ str(i)
		else:
		    st = str(i)
		img = Image.open('../Dataset/awifs_ndvi_2018'+st+'_15_1_clipped.tif')
		img.seek(0)
		for x in range(0,2118):
		    for y in range(0,2135):
		        ar[i-1 + 12][x][y] = img.getpixel((x, y))
	np.save("save_img_arr",ar)
	return ar


def preprocessing():
    images = np.load("save_img_arr.npy")
    preprocessed = []

    for i in range(len(images)):
        temp = images[i]
        temp = blur.blur(temp, blur_kernel_size)
        temp = normalize.normalize(temp)
        temp = change_contrast.change_contrast(temp, contrast)
        height, width = temp.shape
        temp = resize.resize(temp,int(height*resize_factor), int(width*resize_factor))	
        preprocessed.append(temp)
    preprocessed_array = np.array(preprocessed,dtype=np.int64)
    print("Preprocessing done!", len(preprocessed))
    return preprocessed_array

