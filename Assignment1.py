import cv2
import numpy as np

print("hello")

img = cv2.imread('house.jpg',0)

Kx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], np.float32)

print(img)