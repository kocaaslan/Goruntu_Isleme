# Nurullah Kocaaslan
#02205076055

# Görüntü Ters Çevirme
import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('agac.jpg',0)
inverted = np.invert(image)
cv2.imshow("agacnormal",image)
cv2.imshow("agacters",inverted)

# cv2.waitKey()
negimage = 255 - image
cv2.imshow("negimage",negimage)
cv2.waitKey()


