# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 12:32:31 2018
Contours  轮廓
@author: Administrator
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

BLUE = [255,0,0]

img1 = cv2.imread('C:/Users/Administrator/Desktop/picture_exercise/after_work/demo_1.jpg')

image_1 = img1+img1
image_2 = cv2.add(img1,img1)
plt.subplot(131),plt.imshow(img1),plt.title("The original image")
plt.subplot(132),plt.imshow(image_1),plt.title("+ operation")
plt.subplot(133),plt.imshow(image_2),plt.title("add operation"),plt.show()

imgray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
image, contours, hierarchy = cv2.findContours(thresh
                                              ,cv2.RETR_TREE
                                              ,cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[4]
img = cv2.drawContours(image, [cnt], 0, (0,255,0), 3)
plt.imshow(img,'gray'),plt.title('often_show'),plt.show()

















# =============================================================================
# replicate = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REPLICATE)
# reflect = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT)
# reflect101 = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT_101)
# wrap = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_WRAP)
# constant= cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_CONSTANT,value=BLUE)
# 
# plt.subplot(231),plt.imshow(img1,'gray'),plt.title('ORIGINAL')
# plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
# plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
# plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
# plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
# plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')
# 
# plt.show()
# =============================================================================


