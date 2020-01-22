import numpy as np
import preprocessing
import matplotlib.pyplot as plt

def find_harvest():
	imgs = preprocessing.preprocessing()
	#print(imgs[0][300][300],imgs[0][300][300])
	num_images = imgs.shape[0]
	dim_x = imgs.shape[1]
	dim_y = imgs.shape[2]

	diff = np.zeros((num_images-1,dim_x,dim_y))

	j=0
	for i in range(0, num_images-2 ,2):
	    diff[j] = ( imgs[i]) - (imgs[i+2])
	    j+=1
	   
	x = []
	y = []
	threshold = 70
	count = 0
	for k in range(0,24,1):
	    count = 0
	    for i in range(dim_x):
	        for j in range(dim_y):
	            if diff[k][i][j] > 70:
	                count+=1
	    y.append(count)
	    x.append(k)
	print(x,y)
	plt.plot(x,y)
	plt.savefig('plot.png')

find_harvest()
            