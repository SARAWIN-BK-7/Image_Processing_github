import os
import numpy as np
import cv2

img = cv2.imread("medicine_with_noise_mid.jpg")

# We get all the image files from the source folder
# We compute the average by adding up the images
# Start from an explicitly set as floating point, in order to force the
# conversion of the 8-bit values from the images, which would otherwise overflow
average = cv2.imread(img[0]).astype(np.float)
for file in img[1:]:
    image = cv2.imread(img)
    # NumPy adds two images element wise, so pixel by pixel / channel by channel
    average += image
 
# Divide by count (again each pixel/channel is divided)
average /= len(img)

# Normalize the image, to spread the pixel intensities across 0..255
# This will brighten the image without losing information
output = cv2.normalize(average, None, 0, 255, cv2.NORM_MINMAX)

# Save the output
cv2.imwrite('output.png', output)