import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. Load grayscale image
img = cv2.imread("cameraman.jpg", cv2.IMREAD_GRAYSCALE)

if img is None:
    print("cameraman.jpg not found.")
    exit()

# 2. Apply Laplacian edge detection
laplacian = cv2.Laplacian(img, cv2.CV_64F)

#  Convert result to displayable image
laplacian_abs = cv2.convertScaleAbs(laplacian)

# Create figure
plt.figure(figsize=(10, 5))

# Display original image
plt.subplot(1, 2, 1)
plt.imshow(img, cmap="gray")
plt.title("3.1 Original Image")
plt.axis("off")

# Display Laplacian result
plt.subplot(1, 2, 2)
plt.imshow(laplacian_abs, cmap="gray")
plt.title("3.2 Laplacian Result")
plt.axis("off")

# Save result image
plt.savefig("laplacian_result.png")

# Show images
plt.show()