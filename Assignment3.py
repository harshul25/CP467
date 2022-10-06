
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
                    if counter == 0:
                        x_first_bounding_box = i
                        y_first_bounding_box = j 
                    counter +=1
                    x_last_bounding_box = i 
                    y_last_bounding_box = j 
        if (y_first_bounding_box == y_last_bounding_box):
            y_last_bounding_box += 1
        if (x_first_bounding_box == x_last_bounding_box):
            x_last_bounding_box += 1
        y_value.append(float(counter/(abs(x_last_bounding_box - x_first_bounding_box) * abs(y_last_bounding_box - y_first_bounding_box))))
#right image
        [y,x,_] = image_right.shape
        counter = 0
        for i in range(x):
            for j in range(y):
                colour = image_right[j][i]
                #pick on shades of black
                if colour[0] <= 52 and colour[1] <= 52 and colour[2]<=54:
                    counter +=1
        z_value.append(float(counter/(abs(x_last_bounding_box - x_first_bounding_box) * abs(y_last_bounding_box - y_first_bounding_box))))


print(" x  \t y  \t z")
for i in range(len(x_value)-1):
    print("{:0.3f}  {:0.3f}  {:0.3f}".format(x_value[i], y_value[i], z_value[i]))


#Result:
# x       y       z
#0.744  0.071  0.130
#0.728  0.066  0.090
#0.695  0.059  0.114
#0.701  0.039  0.067
#0.737  0.061  0.052
#0.707  0.035  0.061
#0.712  0.088  0.084
#0.723  0.119  0.053
#0.718  0.069  0.107        
