# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 17:57:55 2018

@author: Administrator
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import io,transform,color

img = cv2.imread("C:/Users/Administrator/Desktop/face/01 (1).jpg")
img1 =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
plt.imshow(img1,cmap='gray'),plt.show()




#img1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#img2 = cv2.resize(img1,(36,44))
#plt.imshow(img2,cmap='gray'),plt.show()

#w,h = np.shape(img2)
#he_img = np.zeros((88,36))
#he_img[0:44,0:36] = img2
#he_img[44:88,0:36] = img2
#plt.imshow(he_img),plt.show()
#for i in range(int(1)):
#    for j in range(2):
#        he_img[i*44:(i+1)*44][j*36:(j+1)*36] = a[j]
#plt.imshow(he_img),plt.show()
#new = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#sums = [new,new]
#plt.imshow(sums,cmap='gray'),plt.show()
cv2.imwrite('C:/Users/Administrator/Desktop/3.jpg',img1)


#a = np.arange(5)
#a =a.astype(np.float32)
#b = np.arange(5)
#b =b.astype(np.float32)
##a = float(a)
##b =float(b)
#for i in range(5):
#    a[i] = float(i*0.1)
#    b[i] = float(i*0.2)
#plt.plot(a),plt.plot(b)
#print(1*0.1)