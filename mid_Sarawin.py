import numpy as np 
import cv2 


origi_img = cv2.imread("medicine_with_noise_mid.jpg")
img_gray = cv2.cvtColor(origi_img, cv2.COLOR_BGR2GRAY)

# kernel = np.ones((5,5),np.float32)
dst = blur = cv2.GaussianBlur(img_gray,(5,5),0)


cv2.imshow('Photo_midterm',dst)
cv2.waitKey()