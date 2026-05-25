import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. Load grayscale image
img = cv2.imread("cameraman.jpg", cv2.IMREAD_GRAYSCALE)

if img is None:
    print("cameraman.jpg not found.")
    exit()

# 2.1 Sobel X - detects vertical edges
sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)

# 2.2 Sobel Y - detects horizontal edges
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

# Convert Sobel results to absolute values for display
sobel_x_abs = cv2.convertScaleAbs(sobel_x)
sobel_y_abs = cv2.convertScaleAbs(sobel_y)

# 3. Compute gradient magnitude
gradient_magnitude = np.sqrt(sobel_x**2 + sobel_y**2)

# 4. Convert gradient magnitude to displayable format
gradient_magnitude = cv2.convertScaleAbs(gradient_magnitude)

# Display results
plt.figure(figsize=(12, 8))

# Original image
plt.subplot(2, 2, 1)
plt.imshow(img, cmap="gray")
plt.title("Original Image")
plt.axis("off")

# Sobel X result
plt.subplot(2, 2, 2)
plt.imshow(sobel_x_abs, cmap="gray")
plt.title("Sobel X")
plt.axis("off")

# Sobel Y result
plt.subplot(2, 2, 3)
plt.imshow(sobel_y_abs, cmap="gray")
plt.title("Sobel Y")
plt.axis("off")

# Gradient magnitude result
plt.subplot(2, 2, 4)
plt.imshow(gradient_magnitude, cmap="gray")
plt.title("Gradient Magnitude")
plt.axis("off")

# Save output image
plt.savefig("sobel_results.png")

# Show results
plt.show()

