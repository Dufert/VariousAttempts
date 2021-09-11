# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 23:13:09 2018

@author: Administrator
"""
import numpy as np
import cv2
import matplotlib.pyplot as plt
#plt.hist(img.ravel(),256,[0,256]); plt.show()
i=1
img = cv2.imread('C:/Users/Administrator/Desktop/picture_exercise/license/'+str(i)+'.jpg')

w,h,_ = np.shape(img)
top_left = (150,150)
bottom_right =  (90,90)
#cv2.rectangle(img,top_left, bottom_right, 255, 2)
cv2.line(img,(0,0),(512,512),(255,0,0),5)  
cv2.ellipse(img,top_left,bottom_right,0,0,360,255,2)
plt.imshow(img)

#hist = cv2.calcHist([img],[0],None,[256],[0,256])
#plt.plot(hist)
#
#f = np.fft.fft2(img)
#fshift = np.fft.fftshift(f)
#magnitude_spectrum = 20*np.log(np.abs(fshift))
#
#plt.imshow(magnitude_spectrum[:,:,0] ),plt.show()
#
#rows, cols,_ = np.shape(img)
#crow,ccol = int(rows/2) , int(cols/2)
#fshift[crow-30:crow+30, ccol-30:ccol+30] = 0
#f_ishift = np.fft.ifftshift(fshift)
#img_back = np.fft.ifft2(f_ishift)
#img_back = np.abs(img_back)
#
#plt.subplot(131),plt.imshow(img, cmap = 'gray')
#plt.title('Input Image'), plt.xticks([]), plt.yticks([])
#plt.subplot(132),plt.imshow(img_back, cmap = 'gray')
#plt.title('Image after HPF'), plt.xticks([]), plt.yticks([])
#plt.subplot(133),plt.imshow(img_back)
#plt.title('Result in JET'), plt.xticks([]), plt.yticks([])
#
#plt.show()