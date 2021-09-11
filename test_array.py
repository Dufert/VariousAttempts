# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 21:24:38 2018

@author: Administrator
"""

# -*- coding: utf-8 -*-  
import numpy as np
  
a1 =[[1,2,3],[4,5,6]] #列表  
print('a1 :',np.shape(a1))  
  
a2 = array(a1)   #列表 -----> 数组  
print('a2 :',np.shape(a2))  
  
a3 = mat(a1)      #列表 ----> 矩阵  
print('a3 :',np.shape(a3))  
  
a4 = a3.tolist()   #矩阵 ---> 列表  
print('a4 :',np.shape(a4))  
  
print(a1 == a4)  
#True  
  
a5 = a2.tolist()   #数组 ---> 列表  
  
print('a5 :',a5)  
#('a5 :', [[1, 2, 3], [4, 5, 6]])  
print(a5 == a1)  
#True  
  
a6 = mat(a2)   #数组 ---> 矩阵  
print('a6 :',a6)  
#('a6 :', matrix([[1, 2, 3],[4, 5, 6]]))  
  
print(a6 == a3)  
#[[ True  True  True][ True  True  True]]  
  
a7 = array(a3)  #矩阵 ---> 数组  
print('a7 :',a7)  
#('a7 :', array([[1, 2, 3],[4, 5, 6]]))  
print(a7 == a2)  
#[[ True  True  True][ True  True  True]]  
  
###################################################################  
a1 =[1,2,3,4,5,6] #列表  
print('a1 :',a1)  
#('a1 :', [1, 2, 3, 4, 5, 6])  
  
a2 = array(a1)   #列表 -----> 数组  
print('a2 :',a2)  
#('a2 :', array([1, 2, 3, 4, 5, 6]))  
  
a3 = mat(a1)      #列表 ----> 矩阵  
print('a3 :',a3)  
#('a3 :', matrix([[1, 2, 3, 4, 5, 6]]))  
  
a4 = a3.tolist()   #矩阵 ---> 列表  
print('a4 :',a4)  
#('a4 :', [[1, 2, 3, 4, 5, 6]])   #注意！！有不同  
print(a1 == a4)  
#False  
  
a8 = a3.tolist()[0]   #矩阵 ---> 列表  
print('a8 :',a8)  
#('a8 :', [1, 2, 3, 4, 5, 6])  #注意！！有不同  
print(a1 == a8)  
#True  
  
a5 = a2.tolist()   #数组 ---> 列表  
print('a5 :',a5)  
#('a5 :', [1, 2, 3, 4, 5, 6])  
print(a5 == a1)  
#True  
  
a6 = mat(a2)   #数组 ---> 矩阵  
print('a6 :',a6)  
#('a6 :', matrix([[1, 2, 3, 4, 5, 6]]))  
  
print(a6 == a3)  
#[[ True  True  True  True  True  True]]  
  
a7 = array(a3)  #矩阵 ---> 数组  
print('a7 :',a7)  
#('a7 :', array([[1, 2, 3, 4, 5, 6]]))  
print(a7 == a2)  
#[[ True  True  True  True  True  True]] 