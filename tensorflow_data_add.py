# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 20:47:08 2018

@author: Administrator
"""
import cv2
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt  

img_data = cv2.imread("C:/Users/Administrator/Desktop/picture_exercise/license/1.jpg")
height,width,_ = np.shape(img_data)
#img_data = cv2.cvtColor(img_data,cv2.COLOR_BGR2GRAY)
#print(np.shape(img_data),type(img_data))
#plt.imshow(img_data,cmap='gray'),plt.show()
img = []

with tf.Session() as ses:  
    ses.run(tf.global_variables_initializer())
    img0 = tf.random_crop(img_data,[int(height/2),int(width/2),3])
    img1 = tf.image.random_flip_left_right(img_data)
    img2 = tf.image.random_contrast(img_data, lower=0.5, upper=1.5)  
    img3 = tf.image.random_brightness(img_data, max_delta=32. / 255.)
    img4 = tf.image.random_saturation(img_data, lower=0.5, upper=1.5) 
    img.append(img1)
    img.append(img2)
    img.append(img3)
    img.append(img4)
    img_0 = img0.eval(session=ses)
    img_1 = img1.eval(session=ses)
    img_2 = img2.eval(session=ses)
    img_3 = img3.eval(session=ses)
    img_4 = img4.eval(session=ses)
    plt.imshow(img_0),plt.show()
    plt.imshow(img_1),plt.show()
    plt.imshow(img_2),plt.show()
    plt.imshow(img_3),plt.show()
    plt.imshow(img_4),plt.show()
#img2 = tf.random_crop(img_data)
#img3 = tf.image.random_brightness(img_data)
#img4 = tf.image.random_contrast(img_data)
#img5 = tf.image.per_image_whitening(img_data)