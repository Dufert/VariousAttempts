# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 17:09:45 2018

@author: Administrator
"""
#Demo_skimage matplotlib PIL
import numpy as np
from skimage import io
import cv2
import matplotlib.pyplot as plt

#ax = plt.subplot(111)  
#ax.spines['right'].set_color('none')  
#ax.spines['top'].set_color('none')  
#ax.xaxis.set_ticks_position('bottom')  
#ax.spines['bottom'].set_position(('data',0))  
#ax.yaxis.set_ticks_position('left')  
#ax.spines['left'].set_position(('data',0))  
#x=np.linspace(-np.pi,np.pi,256,endpoint=True)  
#C,S=np.cos(x),np.sin(x)  
#plt.plot(x,C,color='red',linewidth=2.5,linestyle='-')  
#plt.plot(x,S,color='blue',linewidth=2.5,linestyle='-')  
#
#plt.subplot(111)
#x=np.random.normal(0,1,1000)#0,1的正态分布
#y=np.random.normal(0,1,1000)
#plt.scatter(x,y)

#img1.show()
#conF = img1.filter(ImageFilter.CONTOUR)
#edgeF = img1.filter(ImageFilter.FIND_EDGES)
#edgeF.show()
#conF.show()

#io.imshow(img_gray);io.show()
#hsv=color.convert_colorspace(image1,'RGB','HSV')
#io.imshow(hsv)
#io.show()
#L = I.convert('L')   #转化为灰度图
#L = I.convert('1')   #转化为二值化图




#def rgb2gray(rgb):
#    gray_img = np.dot(rgb[...,:3], [0.299, 0.587, 0.114])
#    return gray_img
#
#def adjust(value):  
#    if value > 255:  
#        value = 255  
#    elif value < 0:  
#        value = 0  
#    return value  
#
#def S(x):  
#    x = np.abs(x)  
#    if 0 <= x < 1:  
#        return 1 - 2 * x * x + x * x * x  
#    if 1 <= x < 2:  
#        return 4 - 8 * x + 5 * x * x - x * x * x  
#    else:  
#        return 0  
#    
#def my_bicubic(img,m,n):  
#    height,width = np.shape(img)
#    emptyImage=np.zeros((m,n),np.uint8)  
#    sh=m/height  
#    sw=n/width  
#    for i in range(m):  
#        for j in range(n):  
#            x = i/sh  
#            y = j/sw  
#            p=(i+0.0)/sh-x  
#            q=(j+0.0)/sw-y  
#            x=int(x)-2  
#            y=int(y)-2  
#            A = np.array([  
#                [S(1 + p), S(p), S(1 - p), S(2 - p)]  
#            ])  
#            if x>=m-3:  
#                m-1  
#            if y>=n-3:  
#                n-1  
#            if x>=1 and x<=(m-3) and y>=1 and y<=(n-3):  
#                B = np.array([  
#                    [img[x-1, y-1], img[x-1, y],  
#                     img[x-1, y+1],  
#                     img[x-1, y+1]],  
#                    [img[x, y-1], img[x, y],  
#                     img[x, y+1], img[x, y+2]],  
#                    [img[x+1, y-1], img[x+1, y],  
#                     img[x+1, y+1], img[x+1, y+2]],  
#                    [img[x+2, y-1], img[x+2, y],  
#                     img[x+2, y+1], img[x+2, y+1]],  
#  
#                    ])  
#                C = np.array([  
#                    [S(1 + q)],  
#                    [S(q)],  
#                    [S(1 - q)],  
#                    [S(2 - q)]  
#                ])  
#                cl_img = np.dot(np.dot(A, B[:, :]), C)[0, 0]  
#                cl_img = adjust(cl_img)  
#                emptyImage[i, j] = np.array([cl_img], dtype=np.uint8)  
#    return emptyImage  

def lightCompensate(img,N,M):
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img_row,img_column = np.shape(img)
    light_img = np.zeros((img_row,img_column))
    gray_p = np.mean(img);
    blockage_p = np.zeros((int(img_row/N),int(img_column/M)))
    gray_pa = np.ones((int(img_row/N),int(img_column/M)))
    for i in range(int(img_row/N)):
        for j in range(int(img_column/M)):
            blockage_p[i][j] = np.mean(img[i*N:(i+1)*N-1,j*M:(j+1)*M-1])
    after_p = blockage_p - gray_p*gray_pa
    zoom = cv2.resize(after_p,(img_column,img_row),interpolation=cv2.INTER_CUBIC)
    plt.subplot(121),plt.imshow(zoom, cmap='gray')
    plt.subplot(122),plt.imshow(blockage_p, cmap='gray'),plt.show()
    for i in range(int(img_row)):
        for j in range(int(img_column)):
            light_img[i][j] = img[i][j]-zoom[i][j]
    return light_img

path = "C:/Users/Administrator/Desktop/picture_exercise/license/light.jpg"
image=cv2.imread(path)
new_img = lightCompensate(image,8,8)
plt.subplot(121),plt.imshow(image, cmap='gray')
plt.subplot(122),plt.imshow(new_img, cmap='gray')

