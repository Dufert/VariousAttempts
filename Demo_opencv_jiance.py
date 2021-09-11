# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 10:56:27 2018

@author: Administrator
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt,pylab as plb

#kernel = np.ones((5,5))
#kernel_1 = np.ones((3,3))
#kernel_2 = np.ones((4,4))
#for i in range(7):
#    img = plb.imread('G:/picture_exercise/license/pic/'+str(i+1)+'.jpg')
#    img2 = img
#    img_1 = cv2.Canny(img,250,30)
#    img_1 = cv2.erode(img_1,(3,3))
#    img_1 = cv2.morphologyEx(img_1, cv2.MORPH_CLOSE, kernel)
#    plt.imshow(img_1,cmap = 'gray')
#    plt.show()
#    
#    ret,thresh = cv2.threshold(img2,30,200,0)
#    thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel_1)
#    plt.imshow(thresh,cmap = 'gray')
#    plt.show()
#    thresh = thresh + img_1
#    thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel_2)
#    plt.imshow(thresh,cmap = 'gray')
#    plt.show()

for i in range(1):
    img = plb.imread('G:/picture_exercise/license/pic/'+str(i+1)+'.jpg')
    ret,thresh = cv2.threshold(img,30,200,0)
#    plt.imshow(thresh,cmap = 'gray');plt.show()
    img, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cnt = contours[1]
    epsilon = 0.1*cv2.arcLength(cnt,True)
    approx = cv2.approxPolyDP(cnt,epsilon,True)
    img = cv2.drawContours(img, contours, -1, (0,255,0), 3)
    
    sobelx = cv2.Sobel(img,cv2.CV_8U,1,0,ksize=5)
    sobely = cv2.Sobel(img,cv2.CV_8U,0,1,ksize=5)
    
#    plt.imshow(img,cmap = 'gray'),plt.show()
#    plt.subplot(121),plt.imshow(sobelx,cmap = 'gray')
#    plt.subplot(122),plt.imshow(sobely,cmap = 'gray'),plt.show()
    plt.imshow(sobelx+sobely+img,cmap = 'gray'),plt.show()



























