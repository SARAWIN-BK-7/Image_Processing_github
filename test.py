import cv2 # import library OpenCV 
import numpy as np # import library Numpy 
import test_room_020922 as tr


img = cv2.imread("test_room\cat2.png") # Read the image file
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Convert the gray

half_gray = img_gray[0:600, 0:600] # Set img_gray size
half_color = img[0:600, 600:1200] # Set img size


gray3channel = np.dstack((half_gray, half_gray, half_gray)) # Sort Array 3 channel
new_img = np.hstack((gray3channel, half_color)) # build a new_img by gray3channel and half_color come together

# ---------------------------- Display image --------------------------------------

print(img.shape) # print img.shape, #TODO: check image size(600,1200,3)

# * cv2.imshow('Grayscale image',half_gray) 
# * v2.imshow('test',half_color )
cv2.imshow('cat_twotone', new_img) # display the new_img 
# * cv2.imshow('gray',img_gray)
cv2.waitKey() # waitKey is called when the image is finished
# * cv2.imwrite('filename.png',new_img)
