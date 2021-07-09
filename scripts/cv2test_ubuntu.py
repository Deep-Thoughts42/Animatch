import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("data/img/284121.jpg", cv2.IMREAD_GRAYSCALE)  # = 0
IMREAD_COLOR = 1
IMREAD_UNCHANGED = -1

cv2.imshow("Naruto", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

plt.imshow(img, cmap="gray", interpolation="bicubic")
plt.show()