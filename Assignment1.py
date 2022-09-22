import cv2
import numpy as np

#import image, grayscale it and define filter
img = cv2.imread('house.png')
cv2.imshow("original",img); cv2.waitKey(0); cv2.destroyAllWindows() #if you press enter on the img you can proceed with the code
img = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY) 
cv2.imshow("gray scale",img); cv2.waitKey(0); cv2.destroyAllWindows() #if you press enter on the img you can proceed with the code

filter = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]], np.float32)

#calculate the dimention of operation matrix
img_col_num, img_row_num = img.shape
filter_col_num, filter_row_num = filter.shape

#create pallate for new image and adjust to prevent out of bounds error
y = img_col_num-filter_col_num + 1
x = img_row_num-filter_row_num+1

filtered_img = np.zeros((y,x))

#iterate pixel by pixel and use convolution to apply the filter
for i in range(y):
    for j in range(x):
        filtered_img[i][j] = np.sum(img[i:i+filter_col_num, j:j+filter_row_num]*filter)
        #make sure to check that your pixel values are not above or below the RGB range (0-255)
        if filtered_img[i][j] > 255:
            filtered_img[i][j] = 255
        if filtered_img[i][j] < 0:
            filtered_img[i][j] = 0

cv2.imshow("edges",filtered_img); cv2.waitKey(0); cv2.destroyAllWindows() #if you press enter on the img you can proceed with the code


