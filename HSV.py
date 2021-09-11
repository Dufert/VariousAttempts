# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 22:42:20 2018

@author: Administrator
"""
import matplotlib.image as plb
import cv2
import numpy as np
from matplotlib import pyplot as plt


img=plb.imread("C:/Users/Administrator/Desktop/新建文件夹/新建文件夹 (2)/01/01 (4).jpg")
rows,cols,chanels= np.shape(img)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
imgSkin = np.zeros(img.shape, np.uint8)
imgSkin = img.copy()                       

imgHsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
plt.subplot(121);plt.imshow(imgHsv)
for r in range(rows):
    for c in range(cols):
        H = imgHsv.item(r,c,0)
        S = imgHsv.item(r,c,1)
        V = imgHsv.item(r,c,2)
        
        skin = 0
                
        if True:#((H >= 0) and (H <= 50)) or ((H >= 167) and (H <= 180)):
            if ((S >= 0.1 * 255) and (S <= 0.7 * 255)) and (V >= 0.35 * 255):
                skin = 1
        
        if skin == 0:
            imgSkin.itemset((r,c,0),0)
            imgSkin.itemset((r,c,1),0)                
            imgSkin.itemset((r,c,2),0)
            
plt.subplot(122), plt.imshow(imgSkin)
plt.show()                                                

