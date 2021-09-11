# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 16:43:29 2018

@author: Administrator
"""
#from PIL import Image
import matplotlib.pyplot as pplt
import matplotlib.image as plb
import numpy as np
import scipy.misc as misc

im = plb.imread("H:/picture/1.jpg")
im.shape
pplt.imshow(im)
new_img = misc.imresize(im,0.5)
pplt.imshow(new_img)
def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])

gray = rgb2gray(new_img) 
pplt.imshow(gray)