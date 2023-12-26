import cv2
import numpy as np

# Read an Image
img = cv2.imread('img/fruits.jpg')

# img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# print(img_gray.shape)


# img[:, :, 0] = 0

imgBlue = img[:, :, 0]
imgGreen = img[:, :, 1]
imgRed = img[:, :, 2]
# new_img = np.hstack((img1, img2, img3))
new_img = np.hstack((imgBlue, imgGreen,imgRed))

cv2.imshow('window', new_img)
cv2.waitKey(0)