import numpy as np
'''
These values are all from A3 where
the feature vectors are as follows.

x: is aspect ratio of the image.

y: is the ratio of the left half 
black pixels to the rectangle bounding the image.

z: is the ratio of the right half
 black pixels to the rectangle bounding the image.
'''
cartesian_values_all = [                                                                                        \
                    [0.635, 0.390, 0.208], [0.464, 0.265, 0.326], [0.433, 0.322, 0.312], [0.669, 0.322, 0.312], \
                    [0.565, 0.208, 0.362], [0.854, 0.238, 0.194], [0.453, 0.361, 0.304], [0.549, 0.155, 0.398], \
                    [0.630, 0.226, 0.300], [0.588, 0.202, 0.337]                                                \
                    ]

cartesian_value_given_img = [0.596, 0.173, 0.332]
'''
Calculate Euclidean distance for all
points from the given point

The formula to calculate the distance 
between two points
(x1, y1, z1 ) and (x2, y2, z2) is:
d = √[(x2 - x1)^2 + (y2 - y1)^2 + (z2 - z1)^2].
'''
e_dist = []
point1 = np.array(cartesian_value_given_img)
for p in cartesian_values_all:
    point2 = np.array(p)
    sum_vectors = np.sum(np.square(point1 - point2))
    e_dist.append(np.sqrt(sum_vectors))

for i in range(len(e_dist)):
    print("{}  {:0.3f}".format(i, e_dist[i]))
'''
find the image corresponding to the smallest distance. 
'''
index_of_smallest_dist = e_dist.index(min(e_dist))
print("Image with the smallest distance is: ",index_of_smallest_dist)