# -*- coding: utf-8 -*-
"""
Created on Fri May 18 13:45:07 2018

@author: Administrator
"""

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
w = 284;h = 214;c = 1
suffix = '/*.png'
train_path = 'C:/Users/Administrator/Desktop/picture_exercise/license/face_test/result/'

def read_image(path,w,h):
    
    label_dir = [path+x for x in os.listdir(path) if os.path.isdir(path+x)]
    images = []
    for index,folder in enumerate(label_dir):
        for img in glob.glob(folder+suffix):
            image = cv2.imread(img)
            image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
            image = transform.resize(image,(w,h))
            images.append(image)
    return np.asarray(images,dtype=np.float32)

train_data= read_image(train_path,w,h)
train_image_num = len(train_data)
he_img = np.zeros((w*2,3*h))

for i in range(2):
    for j in range(3):
        he_img[i*w:(i+1)*w,j*h:(j+1)*h] = train_data[i*3+j]*255
plt.imshow(he_img,cmap='gray'),plt.show()
im = transform.resize(he_img,(284*2,214*3,1))     
#cv2.imwrite(train_path+'ss.png',im)
