
import cv2
import numpy as np
import os

directory = 'palm'
x_value = []
y_value = []
z_value = []
#open every image in the directory
for img in os.listdir(directory):
    path = os.path.join(directory,img)
    # we know the image is present
    if os.path.isfile(path):
        #open the image
        image = cv2.imread(path)
        #for half the image analysis we split the image in two on the basis of width.
        [original_y,original_x,_] = image.shape
        max_x,max_y,min_x,min_y = 0,0,original_x,original_y
        for i in range(original_x):
            for j in range(original_y):
                colour = image[j][i]
                if colour[0] <= 52 and colour[1] <= 52 and colour[2]<=54:
                    max_x = max(max_x,i)
                    max_y = max(max_y,j)
                    min_x = min(min_x,i)
                    min_y = min(min_y,j)
        #save all the x values --> aspect ratio width/height
        x_value.append(float(abs(max_x - min_x)/abs(max_y-min_y)))
        centre = int(0.5*(max_x-min_x))
        centre += min_x
        #left image
        counter = 0
        for i in range(min_x,centre):
            for j in range(min_y,max_y):
                colour = image[j][i]
                #pick on shades of black
                if colour[0] <= 52 and colour[1] <= 52 and colour[2]<=54:
                    counter +=1        
        y_value.append(float(counter/(abs(max_x - min_x) * abs(max_y - min_y))))
        #right image
        counter = 0
        for i in range(centre,max_x):
            for j in range(min_y,max_y):
                colour = image[j][i]
                #pick on shades of black
                if colour[0] <= 52 and colour[1] <= 52 and colour[2]<=54:
                    counter +=1
        z_value.append(float(counter/(abs(max_x - min_x) * abs(max_y - min_y))))


print(" x  \t y  \t z")
for i in range(len(x_value)-1):
    print("{:0.3f}  {:0.3f}  {:0.3f}".format(x_value[i], y_value[i], z_value[i]))


"""
Result: 

 x       y       z
0.588  0.202  0.337
0.630  0.226  0.300
0.669  0.325  0.165
0.433  0.322  0.312
0.635  0.390  0.208
0.464  0.265  0.326
0.854  0.238  0.194
0.565  0.208  0.362
0.453  0.361  0.304
"""       
