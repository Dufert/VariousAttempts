# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 10:37:04 2018

@author: Administrator
"""
import cv2
import numpy as np
from skimage import transform
from matplotlib import image as plb,pyplot as plt

img=plb.imread("C:/Users/Administrator/Desktop/face/01 (15).jpg")
rows,cols,chanels= np.shape(img)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
imgSkin = np.zeros(img.shape, np.uint8)
imgSkin = img.copy()     


img_1=plb.imread("C:/Users/Administrator/Desktop/face/kuang.jpg")
img_1 = np.dot(img_1[...,:3], [0.299, 0.587, 0.114])
img_raw,img_col = np.shape(img_1)

for i in range(img_raw):
    for j in range(img_col):
        if img_1[i][j] == 0:
            imgSkin[i,j,0]=0
            imgSkin[i,j,1]=0
            imgSkin[i,j,2]=0
plt.imshow(imgSkin,cmap=None)