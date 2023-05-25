import cv2
import numpy as np

# The path to the map image file
image_path = "my_map3.png"

# Load the image
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Binarize the image
ret, thresh = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)

# Find contours in the image
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# Extract vertices for each contour
for contour in contours:
    epsilon = 0.005 * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)
    if len(approx) >= 4:
        print("New box found:")
        for point in approx:
            x, y = point[0]
            cv2.circle(image, (x, y), 5, (0, 255, 0), -1)
            print(f"Vertex coordinates: ({x}, {y})")

# Save the resulting image
cv2.imwrite("output3.png", image)
