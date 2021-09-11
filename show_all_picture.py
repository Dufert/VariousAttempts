# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 19:05:58 2018

@author: Administrator
"""

import os
import glob
import cv2
import matplotlib.pyplot as plt
import numpy as np
from skimage import io,transform
w = 88;h = 72;c = 1
suffix = '/*.jpg'
train_path = "E:/BaiduYunDownload/mylibrary/train/"
test_path = "E:/BaiduYunDownload/mylibrary/test/"
#train_path = 'E:/BaiduYunDownload/ORL/ORL_train/'
#test_path = 'E:/BaiduYunDownload/ORL/ORL_test/'

def read_image(path,w,h,c):
    
    label_dir = [path+x for x in os.listdir(path) if os.path.isdir(path+x)]
    images = []
    for index,folder in enumerate(label_dir):
        for img in glob.glob(folder+suffix):
            image = cv2.imread(img)
            image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
            image = transform.resize(image,(w,h))
            images.append(image)
            
    return np.asarray(images,dtype=np.float32)

train_data= read_image(train_path,w,h,c)
train_image_num = len(train_data)
he_img = np.zeros((round(w*9),9*h))

for j in range(int(9)):
    for i in range(9):
        he_img[i*w:(i+1)*w,j*h:(j+1)*h] = train_data[j*9+i]
        
plt.figure(figsize=(8, 9))  
plt.imshow(he_img,cmap='gray'),plt.show()

