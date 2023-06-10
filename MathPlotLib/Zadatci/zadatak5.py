#Na jednom prikazu prikažite odvojene histograme crvenog, zelenog i plavog kanala slike
#houses.png

import matplotlib.pyplot as plt
import numpy as np
import cv2


img_bgr=cv2.imread("houses.png",cv2.IMREAD_UNCHANGED)
img_rgb=cv2.cvtColor(img_bgr,cv2.COLOR_BGR2RGB)


blue_channel=img_bgr[:,:,0]
green_channel=img_bgr[:,:,1]
red_channel = img_bgr[:,:,2]


fig,axes=plt.subplots(3)
axes[0].set_title("Blue channel")
axes[0].hist(blue_channel.ravel(),bins=255,range=(0,255))

axes[1].set_title("Green channel")
axes[1].hist(green_channel.ravel(),bins=255,range=(0,255))

axes[2].set_title("Blue channel")
axes[2].hist(red_channel.ravel(),bins=255,range=(0,255))

plt.show()











