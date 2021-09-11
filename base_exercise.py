# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 15:38:20 2018

@author: Administrator
"""
#Demo_numpy
import cv2 
import numpy as np
import matplotlib.pyplot as plt
path = "C:/Users/Administrator/Desktop/picture_exercise/license/light.jpg"
image = cv2.imread(path)
img = cv2.resize(image,(2*image.shape[1],2*image.shape[0]),interpolation=cv2.INTER_CUBIC)
plt.subplot(121),plt.imshow(img, cmap='gray')
plt.subplot(122),plt.imshow(image, cmap='gray')
#a = np.array([[1,2,3],[2,3,4],[5,6,7]])
#b = np.ones((4,3))
#print(a.ndim,a.dtype,a.itemsize,a.size)
#b = np.zeros((4,3))
#c = np.ones((1,2))
#print(b,'\n',c)
#d = np.arange(0,6,1)
#e = np.linspace(0,5,6)
#print(d,'\n',e,'\n',d*e)#点乘
#f=[[1],[2],[3]]
#print(np.dot(a,f),'\n')#矩阵乘法
#print(a.max(axis=0),'\n')#求最大值
#for new_a in a:
#    print(new_a)
#h = [2,4,6]
#print(np.vstack((a,h)),'\n')
#print(np.hstack((a,f)),'\n')
#a.reshape(3,3)
#
#amax,amin = a.max(), a.min()  
#a = (a - amin)/(amax - amin)  
#gols = np.random.normal(loc=0.0, scale=1.0, size=2)
#print (gols,'\n')
#g = a[:1]
#print(g,'\n');
#print(d,'\n',*f)
