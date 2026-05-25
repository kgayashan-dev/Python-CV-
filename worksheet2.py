import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load grayscale image
img = cv2.imread("cameraman.jpg", cv2.IMREAD_GRAYSCALE)

if img is None:
    print("cameraman.jpg not found.")
    exit()

# Sobel X - detects vertical edges
sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)

# Sobel Y - detects horizontal edges 
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

# Convert to absolute values for display
sobel_x_abs = cv2.convertScaleAbs(sobel_x)
sobel_y_abs = cv2.convertScaleAbs(sobel_y)

# Gradient magnitude
gradient_magnitude = np.sqrt(sobel_x**2 + sobel_y**2)
gradient_magnitude = cv2.convertScaleAbs(gradient_magnitude)

# Display  results. Sobel X, Sobel Y, and Gradient Magnitude
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.imshow(img, cmap="gray")
plt.title("Original Image")
plt.axis("off")

# Display Sobel X, Sobel Y, and Gradient Magnitude
plt.subplot(2, 2, 2)
plt.imshow(sobel_x_abs, cmap="gray")
plt.title("Sobel X")
plt.axis("off")

# Display Sobel X, Sobel Y, and Gradient Magnitude
plt.subplot(2, 2, 3)
plt.imshow(sobel_y_abs, cmap="gray")
plt.title("Sobel Y")
plt.axis("off")

# Display Sobel X, Sobel Y, and Gradient Magnitude
plt.subplot(2, 2, 4)
plt.imshow(gradient_magnitude, cmap="gray")
plt.title("Gradient Magnitude")
plt.axis("off")

plt.savefig("sobel_results.png")
plt.show()

# # Laplacian edge detection
# laplacian = cv2.Laplacian(img, cv2.CV_64F)
# laplacian_abs = cv2.convertScaleAbs(laplacian)

# plt.figure(figsize=(10, 5))

# plt.subplot(1, 2, 1)
# plt.imshow(img, cmap="gray")
# plt.title("Original Image")
# plt.axis("off")

# # Display Laplacian result
# plt.subplot(1, 2, 2)
# plt.imshow(laplacian_abs, cmap="gray")
# plt.title("Laplacian Result")
# plt.axis("off")

# # Save the plot
# plt.savefig("laplacian_result.png")
# plt.show()