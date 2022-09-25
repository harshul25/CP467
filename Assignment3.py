
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
        #save all the x values --> aspect ratio width/height
        x_value.append(float(image.shape[1]/image.shape[0]))

        #for half the image analysis we split the image in two on the basis of width.
        centre = int(0.5*len(image))
        [original_y,original_x,_] = image.shape
        image_left = image[0:centre]
        image_right = image[centre:]
#left image
        [y,x,_] = image_left.shape
        counter = 0
        for i in range(x):
            for j in range(y):
                colour = image_left[j][i]
                #pick on shades of black
                if colour[0] <= 52 and colour[1] <= 52 and colour[2]<=54:
                    counter +=1
        y_value.append(float(counter/(original_y * original_x)))
#right image
        [y,x,_] = image_right.shape
        counter = 0
        for i in range(x):
            for j in range(y):
                colour = image_right[j][i]
                #pick on shades of black
                if colour[0] <= 52 and colour[1] <= 52 and colour[2]<=54:
                    counter +=1
        z_value.append(float(counter/(original_y * original_x)))


print(" x  \t y  \t z")
for i in range(len(x_value)-1):
    print("{:0.3f}  {:0.3f}  {:0.3f}".format(x_value[i], y_value[i], z_value[i]))



                
