import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("shapes.png", cv2.IMREAD_GRAYSCALE)

# Top-left edge kernel
top_left_kernel = np.array([
    [ 2,  1,  0],
    [ 1,  0, -1],
    [ 0, -1, -2]
])

# Bottom edge kernel
bottom_kernel = np.array([
    [-1, -1, -1],
    [ 0,  0,  0],
    [ 1,  1,  1]
])

# All-edge kernel
all_edges_kernel = np.array([
    [-1, -1, -1],
    [-1,  8, -1],
    [-1, -1, -1]
])

top_left_edges = cv2.filter2D(img, -1, top_left_kernel)

bottom_edges = cv2.filter2D(img, -1, bottom_kernel)

all_edges = cv2.filter2D(img, -1, all_edges_kernel)

plt.figure(figsize=(12,8))

plt.subplot(2,2,1)
plt.imshow(img, cmap='gray')
plt.title("Original")
plt.axis("off")

plt.subplot(2,2,2)
plt.imshow(top_left_edges, cmap='gray')
plt.title("Top Left Edges")
plt.axis("off")

plt.subplot(2,2,3)
plt.imshow(bottom_edges, cmap='gray')
plt.title("Bottom Edges")
plt.axis("off")

plt.subplot(2,2,4)
plt.imshow(all_edges, cmap='gray')
plt.title("All Edges")
plt.axis("off")

plt.show()