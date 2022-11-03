# Nurullah Kocaaslan
#02205076055

# histogram hesaplama
import cv2
import numpy as np
from matplotlib import pyplot as plt

foto = cv2.imread("cicek.jpg",0)
Hist = np.zeros(256)
[w,h] = np.shape(cicek)
for v in range (0,h):
    for u in range (0,w):
        i = cicek[u,v]
        Hist[i]=Hist[i]+1
cv2.imshow("cicek",cicek)

plt.plot(H)
plt.show()
cv2.waitKey(0)

