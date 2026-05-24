import cv2
import numpy as np
from matplotlib import pyplot as plt


# Load the image in grayscale mode
# cv2.IMREAD_GRAYSCALE converts the image into black and white
img = cv2.imread("fig1.2.jpg", cv2.IMREAD_GRAYSCALE)


# =========================
# TOP-LEFT EDGE DETECTION KERNEL
# =========================
# This kernel highlights edges that change from
# top-left to bottom-right direction.

top_left_kernel = np.array([
    [ 2,  1,  0],
    [ 1,  0, -1],
    [ 0, -1, -2]
])


# =========================
# BOTTOM EDGE DETECTION KERNEL
# =========================
# This kernel detects horizontal edges,
# especially bottom edges.

bottom_kernel = np.array([
    [-1, -1, -1],
    [ 0,  0,  0],
    [ 1,  1,  1]
])


# =========================
# ALL-EDGE DETECTION KERNEL
# =========================
# This is a classic edge-detection kernel.
# It highlights strong intensity changes
# in all directions.

all_edges_kernel = np.array([
    [-1, -1, -1],
    [-1,  8, -1],
    [-1, -1, -1]
])


# =========================
# APPLY FILTERS USING CONVOLUTION
# =========================
# cv2.filter2D() slides the kernel across the image.
#
# For each pixel:
# 1. Multiply neighboring pixels by kernel values
# 2. Add all results
# 3. Store the sum as the new pixel value
#
# This operation is called convolution.

top_left_edges = cv2.filter2D(img, -1, top_left_kernel)

bottom_edges = cv2.filter2D(img, -1, bottom_kernel)

all_edges = cv2.filter2D(img, -1, all_edges_kernel)


# =========================
# DISPLAY RESULTS
# =========================

# Create a large figure window
plt.figure(figsize=(12,8))


# Show original image
plt.subplot(2,2,1)
plt.imshow(img, cmap='gray')
plt.title("Original")
plt.axis("off") #on / off axis display


# Show top-left edge detection result
plt.subplot(2,2,2)
plt.imshow(top_left_edges, cmap='gray')
plt.title("Top Left Edges")
plt.axis("off")


# Show bottom edge detection result
plt.subplot(2,2,3)
plt.imshow(bottom_edges, cmap='gray')
plt.title("Bottom Edges")
plt.axis("off")


# Show all-edge detection result
plt.subplot(2,2,4)
plt.imshow(all_edges, cmap='gray')
plt.title("All Edges")
plt.axis("off")


# Display all images on screen
plt.show()