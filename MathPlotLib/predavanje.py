import matplotlib.pyplot as plt
import numpy as np
import cv2

#plt.plot([1,2,3,10],[7,-4,3,0])
#plt.show

"""
x_values=np.linspace(0,2,50)
y_linear_values=x_values
y_square_values=np.power(x_values,2)
"""

"""
plt.plot(x_values,y_linear_values,label='Linear values')
plt.plot(x_values,y_square_values,label='Square values')
plt.xlabel("x")
plt.ylabel("y")
plt.title("Linear and Square values")
plt.legend()
plt.show()
"""
"""
fig,axes =plt.subplots(2)
fig.suptitle("Dva prikaza")

axes[0].set_title("Linearno")
axes[0].plot(x_values,y_linear_values)
axes[0].set(xlabel="x",ylabel="y")

axes[1].set_title("Kvadratno")
axes[1].plot(x_values,y_square_values)
axes[1].set(xlabel="x square",ylabel="y square")

plt.show()
"""


"""
Random histogram
data=np.random.randn(1000)
plt.hist(data, bins=200)
plt.title("Histogram")
plt.show()
"""

"""
#histrogram slike u geyscaleu
img=cv2.imread("kamera4.png",cv2.IMREAD_GRAYSCALE)
plt.hist(img.ravel(),bins=256,range=(0,255))
plt.show()
"""

"""
Pokazivanja slika u matplotlib 
img_bgr=cv2.imread("kamera4.png")
img_rgb=cv2.cvtColor(img_bgr,cv2.COLOR_BGR2RGB)
img_gray=cv2.cvtColor(img_bgr,cv2.COLOR_BGR2GRAY)
fig,axes= plt.subplots(2)
axes[0].imshow(img_rgb)
axes[1].imshow(img_gray,cmap='gray')
plt.show()
"""

img_bgr=cv2.imread("stop.png")
img_rgb=cv2.cvtColor(img_bgr,cv2.COLOR_BGR2RGB)
img_hsv=cv2.cvtColor(img_bgr,cv2.COLOR_BGR2HSV)

img_h_vaues_original=img_hsv[:,:,0]


red_mask=cv2.inRange(img_hsv,np.array([0,100,100]),np.array([7,255,255]))
img_red_filter_hsv=cv2.bitwise_and(img_hsv,img_hsv,mask=red_mask)
img_red_filter_rgb=cv2.cvtColor(img_red_filter_hsv,cv2.COLOR_HSV2RGB)

img_h_vaues_filtered=img_red_filter_hsv[:,:,0]


fig,axes=plt.subplots(2,2)

axes[0][0].set_title("Original image")
axes[0][0].imshow(img_rgb)

axes[0][1].set_title("Original H histogram")
axes[0][1].hist(img_h_vaues_original.ravel(),bins=180,range=(0,179))


axes[1][0].set_title("Filtered image")
axes[1][0].imshow(img_red_filter_rgb)

axes[1][1].set_title("Filtered H histogram")
axes[1][1].hist(img_h_vaues_filtered.ravel(),bins=180,range=(0,179))
plt.show()








