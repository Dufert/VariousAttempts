# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 14:37:06 2018

@author: Administrator
"""
import numpy as np
j = np.array([[1, 2],
              [3, 5],
              [6, 7]])
change_img = np.zeros((5,5))
for i in range(2):
    change_img[1,i] = j[1,i]
print(change_img)
print(j.flatten())