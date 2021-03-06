# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 12:04:11 2018

@author: Administrator
"""
import numpy as np
#import matplotlib.pyplot as plt
import matplotlib.image as mgimg
import gParam
import copy
import scipy.signal as signal
import cv2 as cv

# createst uniform random array w/ values in [a,b) and shape args a，b之间创建随机数
# return value type is ndarray 反回对象类
def rand_arr(a, b, *args): 
    np.random.seed(0) 
    return np.random.rand(*args) * (b - a) + a

# Class Cnn     
class Ccnn:
	def __init__(self, cLyNum, pLyNum,fLyNum,oLyNum):
		self.cLyNum = cLyNum#卷积层个数
		self.pLyNum = pLyNum
		self.fLyNum = fLyNum
		self.oLyNum = oLyNum
		self.pSize = gParam.P_SIZE
		self.yita = 0.01
		self.cLyBias = rand_arr(-0.1, 0.1, 1,cLyNum)
		self.fLyBias = rand_arr(-0.1, 0.1, 1,fLyNum)
		self.kernel_c = np.zeros((gParam.C_SIZE,gParam.C_SIZE,cLyNum))
		self.kernel_f = np.zeros((gParam.F_NUM,gParam.F_NUM,fLyNum))
		for i in range(cLyNum):
			self.kernel_c[:,:,i] = rand_arr(-0.1,0.1,gParam.C_SIZE,gParam.C_SIZE)
		for i in range(fLyNum):
			self.kernel_f[:,:,i] = rand_arr(-0.1,0.1,gParam.F_NUM,gParam.F_NUM)
		self.pooling_a = np.ones((self.pSize,self.pSize))/(self.pSize**2)	
		self.weight_f = rand_arr(-0.1,0.1, pLyNum, fLyNum)
		self.weight_output = rand_arr(-0.1,0.1,fLyNum,oLyNum)
        
	def read_pic_data(self, path, i):
#		print (read_pic_data)
		data = np.array([])
		full_path = path + '%d'%i + gParam.FILE_TYPE
		try:
			data = mgimg.imread(full_path) #data is np.array
			data = (np.double)(data)
		except IOError:
			raise Exception('open file error in read_pic_data():', full_path)
		return data		
    
	def read_label(self, path):
		#print 'read_label'
		ylab = []
		try:
			fobj = open(path, 'r')
			for line in fobj:
				ylab.append(line.strip())
			fobj.close()
		except IOError:
			raise Exception('open file error in read_label():', path)		
		return ylab		
    
	#卷积层
#    所谓权值共享就是指 一张图片上的所有位置被同一个滤波器扫 而一次这个图上每一个位置的权值是一样的
	def convolution(self, data, kernel):
#        print ("convolution")
		data_row, data_col = np.shape(data)
		kernel_row, kernel_col = np.shape(kernel)
		n = data_col - kernel_col
		m = data_row - kernel_row
		state = np.zeros((m+1, n+1))
		for i in range(m+1):
			for j in range(n+1):
				temp = np.multiply(data[i:i+kernel_row,j:j+kernel_col], kernel)
				state[i][j] = temp.sum()
		return state		
    
	# 池化层			
	def pooling(self, data, pooling_a):		
#        print ("pooling")
		data_r, data_c = np.shape(data)
		p_r, p_c = np.shape(pooling_a)
		r0 = int(data_r/p_r)
		c0 = int(data_c/p_c)
		state = np.zeros((r0,c0))
		for i in range(c0):
			for j in range(r0):
				temp = np.multiply(data[p_r*i:p_r*i+1,p_c*j:p_c*j+1],pooling_a)
				state[i][j] = temp.sum()
		return state
    
	#全连接层
	def convolution_f1(self, state_p1, kernel_f1, weight_f1):
		#池化层出来的20个特征矩阵乘以池化层与全连接层的连接权重进行相加
		#wx(这里的偏置项=0),这个结果然后再和全连接层中的神经元的核
		#进行卷积,返回值:
		#1：全连接层卷积前,只和weight_f1相加之后的矩阵
		#2：和全连接层卷积完之后的矩阵		
		n_p0, n_f = np.shape(weight_f1)#n_p0=20(是Feature Map的个数);n_f是100(全连接层神经元个数)
		m_p, n_p, pCnt = np.shape(state_p1)#这个矩阵是三维的
		m_k_f1, n_k_f1,fCnt = np.shape(kernel_f1)#12*12*100
		state_f1_temp = np.zeros((m_p,n_p,n_f))
		state_f1 = np.zeros((m_p - m_k_f1 + 1,n_p - n_k_f1 + 1,n_f))	
		for n in range(n_f):
			count = 0
			for m in range(n_p0):
				temp = state_p1[:,:,m] * weight_f1[m][n] 
				count = count + temp
			state_f1_temp[:,:,n] = count
			state_f1[:,:,n] = self.convolution(state_f1_temp[:,:,n], kernel_f1[:,:,n])	
		return state_f1, state_f1_temp	
	# softmax 层
	def softmax_layer(self,state_f1):
		# print 'softmax_layer'
		output = np.zeros((1,self.oLyNum))
		t1 = (np.exp(np.dot(state_f1,self.weight_output))).sum()
		for i in range(self.oLyNum):
			t0 = np.exp(np.dot(state_f1,self.weight_output[:,i]))
			output[:,i]=t0/t1
		return output	

	#误差反向传播更新权值
	def cnn_upweight(self,err_cost, ylab, train_data,state_c1, \
					state_s1, state_f1, state_f1_temp, output):
		#print 'cnn_upweight'
			m_data, n_data = np.shape(train_data)
			# softmax的资料请查看 (TODO)
			label = np.zeros((1,self.oLyNum))
			label[:,ylab]	= 1 
			delta_layer_output = output - label
			weight_output_temp = copy.deepcopy(self.weight_output)
			delta_weight_output_temp = np.zeros((self.fLyNum, self.oLyNum))
			#print shape(state_f1)
			#更新weight_output			
			for n in range(self.oLyNum):
				delta_weight_output_temp[:,n] = delta_layer_output[:,n] * state_f1
			weight_output_temp = weight_output_temp - self.yita * delta_weight_output_temp
			
			#更新bais_f和kernel_f (推导公式请查看 TODO)	
			delta_layer_f1 = np.zeros((1, self.fLyNum))
			delta_bias_f1 = np.zeros((1,self.fLyNum))
			delta_kernel_f1_temp = np.zeros(np.shape(state_f1_temp))
			kernel_f_temp = copy.deepcopy(self.kernel_f)			
			for n in range(self.fLyNum):
				count = 0
				for m in range(self.oLyNum):
					count = count + delta_layer_output[:,m] * self.weight_output[n,m]
				delta_layer_f1[:,n] = np.dot(count, (1 - np.tanh(state_f1[:,n])**2))	
				delta_bias_f1[:,n] = delta_layer_f1[:,n]
				delta_kernel_f1_temp[:,:,n] = delta_layer_f1[:,n] * state_f1_temp[:,:,n]
			# 1
			self.fLyBias = self.fLyBias - self.yita * delta_bias_f1
			kernel_f_temp = kernel_f_temp - self.yita * delta_kernel_f1_temp
			 
			#更新weight_f1
			delta_layer_f1_temp = np.zeros((gParam.F_NUM,gParam.F_NUM,self.fLyNum))
			delta_weight_f1_temp = np.zeros(np.shape(self.weight_f))
			weight_f1_temp = copy.deepcopy(self.weight_f)
			for n in range(self.fLyNum):
				delta_layer_f1_temp[:,:,n] = delta_layer_f1[:,n] * self.kernel_f[:,:,n]
			for n in range(self.pLyNum):
				for m in range(self.fLyNum):
					temp = delta_layer_f1_temp[:,:,m] * state_s1[:,:,n]
					delta_weight_f1_temp[n,m] = temp.sum()
			weight_f1_temp = weight_f1_temp - self.yita * delta_weight_f1_temp

			# 更新bias_c1
			n_delta_c = m_data - gParam.C_SIZE + 1
			delta_layer_p = np.zeros((gParam.F_NUM,gParam.F_NUM,self.pLyNum))
			delta_layer_c = np.zeros((n_delta_c,n_delta_c,self.pLyNum))
			delta_bias_c = np.zeros((1,self.cLyNum))
			for n in range(self.pLyNum):
				count = 0
				for m in range(self.fLyNum):
					count = count + delta_layer_f1_temp[:,:,m] * self.weight_f[n,m]
				delta_layer_p[:,:,n] = count
				#print shape(np.kron(delta_layer_p[:,:,n], ones((2,2))/4))
				delta_layer_c[:,:,n] = np.kron(delta_layer_p[:,:,n], np.ones((2,2))/4) \
									  * (1 - np.tanh(state_c1[:,:,n])**2)
				delta_bias_c[:,n] = delta_layer_c[:,:,n].sum()
			# 2
			self.cLyBias = self.cLyBias - self.yita * delta_bias_c
			#更新 kernel_c1
			def nlist(x):
				return list(x)
			delta_kernel_c1_temp = np.zeros(np.shape(self.kernel_c))
			for n in range(self.cLyNum):
				temp = delta_layer_c[:,:,n]
				r1 = map(nlist,zip(*temp[::1]))#逆时针旋转90度	
				r2 = map(nlist,zip(*r1[::1]))#再逆时针旋转90度
				temp = signal.convolve2d(train_data, r2,'valid')
				temp1 = map(nlist,zip(*temp[::1]))
				delta_kernel_c1_temp[:,:,n] = map(nlist,zip(*temp1[::1]))
			self.kernel_c = self.kernel_c - self.yita * delta_kernel_c1_temp							  					
			self.weight_f = weight_f1_temp
			self.kernel_f = kernel_f_temp
			self.weight_output = weight_output_temp				

		# predict
	def cnn_predict(self,data):
		return 
			
		