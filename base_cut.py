# -*- coding: utf-8 -*-
"""
Created on Sun May 20 00:05:02 2018

@author: Administrator
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt 
for hh in range(1,7):
    img = cv2.imread('C:/Users/Administrator/Desktop/picture_exercise/license/s'+str(hh+1)+'.jpg')
    g = 1
    img_raw,img_col,_ = np.shape(img)
    gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    _,threshold_img = cv2.threshold(gray_img,127,255,cv2.THRESH_BINARY)
    Canny_img = cv2.erode(threshold_img,(8,5))
    Canny_img = cv2.erode(Canny_img,(2,2))
    Canny_img = cv2.erode(Canny_img,(2,2))
    plt.subplot(221),plt.imshow(img)
    plt.subplot(222),plt.imshow(gray_img,cmap='gray')
    plt.subplot(223),plt.imshow(threshold_img,cmap='gray')
    plt.subplot(224),plt.imshow(Canny_img,cmap='gray'),plt.show()
    
    a = np.zeros((1,img_col))
    b = np.zeros((1,img_raw))
    for i in range(img_col):
        a[0,i] = np.sum(Canny_img[:,i])/255
    
    for j in range(img_raw):
        b[0,j] = np.sum(Canny_img[j,:])/255
    
    #my idea 
    check = np.ones((img_raw,1))
    c = np.zeros((1,img_col))
    for j in range(img_col):
        c[0,j]= np.sum(Canny_img[16:68,j:j+1]*check[16:68,:])/255
    plt.plot(range(img_col),c[0,:]),plt.show()
    #    print(np.where(0==c[0,:]))
    
    address_raw = [0,0,0,0,0,0,0,0,img_col]
    for k in range(img_col):
#        print('k:',k,'g:',g,'cha:',(k - address_raw[g-1]))
        if (k - address_raw[g-1])>60:
            address_raw[g] = address_raw[g-1]+32
            g+=1
            print('enter0')
        elif ((g<3)and((k-address_raw[g-1])>32)and(c[0,k]<3)):
            address_raw[g] = k
            g+=1
            print('enter1')
        elif  ((g==3)and((k-address_raw[g-1])>12)):
            if(c[0,k]<1):
                address_raw[g] = k
                g+=1
            elif ((k-address_raw[g-1])>20):
                address_raw[g] = address_raw[g-1]+12
                g+=1
            print('enter2')
        elif ((g>3)and((k-address_raw[g-1])>32)and(c[0,k]<3)):
            address_raw[g]=k
            g+=1
            print('enter3')
        elif g==8:
            break
        else:
            pass
    print(address_raw)
        
    cut = []
    for h in range(8):
        cut_1 = Canny_img[16:80,int(address_raw[h]):int(address_raw[h+1])]
        plt.subplot(2,4,h+1),plt.imshow(cut_1,cmap='gray')
        cut.append(cut_1)
    plt.show()