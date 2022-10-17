import numpy as np 
import cv2 

# NOTE -  Read the image file
origi_img = cv2.imread("medicine_with_noise_mid.jpg")

# NOTE - Convert the original image to grayscale  
img_gray = cv2.cvtColor(origi_img, cv2.COLOR_BGR2GRAY)

# NOTE - Create kernel array or matrix 5*5 by all members = 1
kernel = np.ones((5,5),np.float32) 

                     

# NOTE - test GaussianBlur by opencv
# dst = blur = cv2.GaussianBlur(origi_img,(5,5),0)

# NOTE -  Display image output
cv2.imshow('Photo_midterm',origi_img)
cv2.waitKey()