# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 20:03:37 2023

@author: Lenovo
"""

import numpy as np
import matplotlib.pyplot as plt

# 定义样本及其标签
X = np.array([[3, 3], [4, 3], [1, 1]])
y = np.array([1, 1, -1])

# 初始化权重w和偏置b为0
w = np.zeros(X.shape[1])
b = 0
w_old=np.zeros(X.shape[1])
b_old=0
# 设置学习率和最大迭代次数
lr = 1
max_iter = 20

# 迭代更新权重和偏置
for i in range(max_iter):
    # 遍历所有样本
    print("i="+str(i))
    for j in range(len(X)):
        print("j="+str(j))
        # 计算预测值
        y_pred = np.dot(w, X[j]) + b
        print("y_pred="+str(y_pred)+"="+str(w)+"*"+str(X[j])+"+"+str(b))
        # 如果预测值与真实标签不一致，则更新权重和偏置
        if y[j] * y_pred <= 0:
            
            print("w="+str(w)+"+"+str(lr)+"*"+str(y[j])+"*"+str(X[j]))
            w += lr * y[j] * X[j]
            print("w="+str(w))
            
            print("b="+str(b)+"+"+str(lr)+"*"+str(y[j]))
            b += lr * y[j]
            print("b="+str(b))
    #如果训练一遍后，w或b保持变了，记录w与b，否则跳出大循环
    if b_old!=b or False in (w==w_old):
        #print("w_old="+str(w_old))
        #print("w="+str(w))
        print(False in (w==w_old))
        b_old=b
        for k in range(w.shape[0]):
            w_old[k]=w[k]
    else:
        break        
# 绘制样本点和分离超平面
plt.scatter(X[:2, 0], X[:2, 1], c='b', marker='o', label='positive')
plt.scatter(X[2, 0], X[2, 1], c='r', marker='x', label='negative')
x = np.linspace(0, 5, 10)
y = -(w[0] * x + b) / w[1]
plt.plot(x, y, c='g', label='separating hyperplane')
plt.legend()
plt.show()
