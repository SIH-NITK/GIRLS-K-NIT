import numpy as np
import preprocessing
import matplotlib.pyplot as plt

def find_harvest():
	imgs = preprocessing.preprocessing()
	print(imgs.shape)
	print(imgs[0][300][300][0],imgs[0][300][300][1])
	num_images = imgs.shape[0]
	dim_x = imgs.shape[1]
	dim_y = imgs.shape[2]

	diff = np.zeros((num_images-1,dim_x,dim_y))

	for i in range(num_images - 1):
	    diff[i] = imgs[i+1] - imgs[i]
	   
	x = []
	y = []
	threshold = 70
	count = 0
	for k in range(0,23,1):
	    count = 0
	    for i in range(dim_x):
	        for j in range(dim_y):
	            if diff[k][i][j] > 70:
	                count+=1
	    y.append(count)
	    x.append(k)

find_harvest()
            