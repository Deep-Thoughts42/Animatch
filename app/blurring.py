# %%
import cv2
import numpy as np



size_list = [(8, 8), (16, 16), (32, 32), (64, 64), (128, 128)]


# file path to the image
img = cv2.imread('data/img/naruto.jpg')

height, width = img.shape[:2]

w, h = (16, 16)

temp = cv2.resize(img, (w, h), interpolation=cv2.INTER_LINEAR)

output = cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)

cv2.imshow('Input', img)
cv2.imshow('Output', output)

cv2.waitKey(0)



# # name of frame and then the img requested
# cv2.imshow("TestNaruto", img)

# kernel = np.ones((20, 20), np.float32) / 225
# smoothed = cv2.filter2D(img, -1, kernel)

# # Gaussian Blur
# blur = cv2.GaussianBlur(img, (21, 21), 0)
# # Median blur
# median = cv2.medianBlur(img, 21)
# # bilateral blur
# bilat = cv2.bilateralFilter(img, 15, 75, 75)


# # cv2.imshow('frame', frame)
# cv2.imshow('res', img)
# cv2.imshow('smoothed', smoothed)
# cv2.imshow('blur', blur)
# cv2.imshow("median", median)
# cv2.imshow('bilateral', bilat)


# # if any key is pressed, exit out of the program
# cv2.waitKey(0)
# cv2.destroyAllWindows()