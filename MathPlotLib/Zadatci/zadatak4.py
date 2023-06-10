#Na jednom prikazu prikažite sliku raskrizje.png:
#1. u boji,
#2. u sivim nijansama,
import matplotlib.pyplot as plt
import numpy as np
import cv2


img_bgr=cv2.imread("raskrizje.png")
img_rgb=cv2.cvtColor(img_bgr,cv2.COLOR_BGR2RGB)
img_gray=cv2.cvtColor(img_bgr,cv2.COLOR_BGR2GRAY)
fig,axes= plt.subplots(2)
axes[0].imshow(img_rgb)
axes[1].imshow(img_gray,cmap='gray')
plt.show()
































