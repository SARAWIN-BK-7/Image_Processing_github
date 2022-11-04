import numpy as np
import cv2
import matplotlib.pyplot as plt

# NOTE -  Read the image file
origi_img = cv2.imread("medicine_with_noise_mid.jpg")

# NOTE - Convert the original image to grayscale
img_gray = cv2.cvtColor(origi_img, cv2.COLOR_BGR2GRAY)

# NOTE - Create kernel array or matrix 5*5 by all members = 1
# kernel = np.ones((5,5),np.float32)

# NOTE - test GaussianBlur by opencv
dst = cv2.GaussianBlur(origi_img,(25,25),0)

# NOTE -  Display image output
cv2.imshow('Photo_midterm',dst)
cv2.imwrite('mediBlue.jpg',dst)
cv2.waitKey()


# img = cv2.imread("medicine_with_noise_mid.jpg", -1)
# fig = plt.figure(figsize=(15, 15))


# def notched_rejected(shape, d0, u_k, v_k):
#     M, N = shape
#     H = np.zeros((M, N))

#     for u in range(0, M):
#         for v in range(0, N):

#             D_uv = np.sqrt((u-M/2+u_k)**2+(v-N/2+v_k)**2)
#             D_muv = np.sqrt((u-M/2-u_k)**2+(v-N/2+v_k)**2)

#             if (D_uv < d0 or D_muv < 0):
#                 H[u, v] = 0.0
#             else:
#                 H[u, v] = 1.0
#     return H


# f = np.fft.fft2(img)
# fshift = np.fft.fftshift(f)
# magnitude_spectrum = 20*np.log(abs(fshift))

# img_shape = img.shape
# H1 = notched_rejected(img_shape, 9, 10, 10)

# notched_filter = H1
# notched_rejected_center = fshift*notched_filter

# cv2.imshow('Photo_midterm', magnitude_spectrum)
# cv2.waitKey()
