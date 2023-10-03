# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 15:41:49 2023

@author: Lenovo
"""

#导入必要的库和模块
from sklearn.datasets import make_blobs # 用于生成人工数据
from sklearn.neighbors import KNeighborsClassifier # 用于实现KNN算法
import matplotlib.pyplot as plt # 用于数据可视化
from sklearn.model_selection import train_test_split # 用于将数据集分为训练集和测试集
#使用make_blobs函数生成人工数据
data = make_blobs(n_samples=100, centers=2, random_state=9)
#'n_samples'指定要生成的样本数
#'centers'指定要生成的中心点数
#'random_state'是随机数生成器使用的种子
#将生成的数据分为特征和标签
X, y = data
#'X'包含特征矩阵（输入数据）
#'y'包含标签向量（输出数据）
#使用散点图可视化生成的数据
plt.scatter(X[y==1,0], X[y==1,1], cmap=plt.cm.spring, edgecolor='k', marker='^')
#绘制类别1的特征，使用'^'标记
plt.scatter(X[y==0,0], X[y==0,1], cmap=plt.cm.spring, edgecolor='k', marker='o')
#绘制类别0的特征，使用'o'标记
plt.show()
#显示散点图

import numpy as np
# 导入必要的库，包括numpy、KNN分类器和matplotlib.pyplot
clf = KNeighborsClassifier()
# 创建KNN分类器
clf.fit(X, y)
# 使用数据进行训练，其中X是样本特征，y是样本标签
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 0].max() + 1
# 确定图像的范围
xx, yy = np.meshgrid(np.arange(x_min, x_max, .02), np.arange(y_min, y_max, .02))
# 构建网格点
Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
# 对网格点进行分类预测
Z = Z.reshape(xx.shape)
# 调整Z的形状以匹配xx的形状
plt.pcolormesh(xx, yy, Z, cmap=plt.cm.Set3)
# 根据预测结果对网格进行着色
plt.scatter(X[y == 1, 0], X[y == 1, 1], cmap=plt.cm.spring, edgecolor='k', marker='^')
plt.scatter(X[y == 0, 0], X[y == 0, 1], cmap=plt.cm.spring, edgecolor='k', marker='o')
# 在图上绘制原始数据集的散点图
plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
plt.title('Classifier:KNN')
# 设置标题
plt.scatter(-5.49, -3.67, marker='*', c='red', s=100)
# 绘制新数据点
plt.show()
# 显示图像
print('新数据点[-5.49, -3.67]的分类是：', clf.predict([[-5.49, -3.67]]))
# 输出新数据点的分类结果
data2 = make_blobs(n_samples=300, centers=4, random_state=4)
X2, y2 = data2
# 创建第二个数据集
plt.scatter(X2[y2 == 0, 0], X2[y2 == 0, 1], edgecolor='k', marker='o')
plt.scatter(X2[y2 == 1, 0], X2[y2 == 1, 1], edgecolor='k', marker='^')
plt.scatter(X2[y2 == 2, 0], X2[y2 == 2, 1], edgecolor='k', marker='s')
plt.scatter(X2[y2 == 3, 0], X2[y2 == 3, 1], edgecolor='k', marker='D')
# 在图上绘制第二个数据集的散点图
plt.show()
# 显示图像
clf = KNeighborsClassifier()
# 创建新的KNN分类器
clf.fit(X2, y2)
#对数据进行网格，化并预测每个网格点的类别
#其中xx是以x_min到x_max每隔0.02个单位的一维数组为第一维，以y_min到y_max每隔0.02个单位的一维数组为第二维的网格矩阵
#yy同理，是以y_min到y_max每隔0.02个单位的一维数组为第一维，以x_min到x_max每隔0.02个单位的一维数组为第二维的网格矩阵
x_min,x_max=X2[:,0].min()-1,X2[:,0].max()+1
y_min,y_max=X2[:,1].min()-1,X2[:,0].max()+1
xx,yy=np.meshgrid(np.arange(x_min,x_max,.02),
np.arange(y_min,y_max,.02))
#预测每个网格点的类别，并将结果reshape成与网格矩阵xx同样的形状
Z=clf.predict(np.c_[xx.ravel(),yy.ravel()])
Z=Z.reshape(xx.shape)
#画出网格矩阵和对应类别的散点图
plt.pcolormesh(xx,yy,Z,cmap=plt.cm.Set3)
plt.scatter(X2[y2==1,0],X2[y2==1,1],edgecolor='k',marker='^')
plt.scatter(X2[y2==0,0],X2[y2==0,1],edgecolor='k',marker='o')
plt.scatter(X2[y2==2,0],X2[y2==2,1],edgecolor='k',marker='s')
plt.scatter(X2[y2==3,0],X2[y2==3,1],edgecolor='k',marker='D')
#设置横纵坐标轴的上下限
plt.xlim(xx.min(),xx.max())
plt.ylim(yy.min(),yy.max())
#设置图的标题
plt.title('Classifier:KNN')
plt.show()
#输出模型在测试集上的正确率
print('模型正确率：{:.2f}'.format(clf.score(X2,y2)))

from sklearn.datasets import make_regression
X, y = make_regression(n_features=1, n_informative=1, noise=30, random_state=5)
# 散点图展示数据集
plt.scatter(X, y, c='b', edgecolor='k')
plt.show()

from sklearn.neighbors import KNeighborsRegressor
reg = KNeighborsRegressor()
reg.fit(X, y)
# 使用等距点生成预测结果
z = np.linspace(-2.5, 2.5, 200).reshape(-1, 1)
plt.scatter(X, y, c='b', edgecolor='k')
plt.plot(z, reg.predict(z), c='r', linewidth=3)
plt.title('KNN Regressor')
plt.show()
# 输出模型评分
print('模型评分：{:.2f}'.format(reg.score(X, y)))


#导入KNN回归器
from sklearn.neighbors import KNeighborsRegressor
#创建一个KNN回归器实例，并设置邻居个数为2
reg2 = KNeighborsRegressor(n_neighbors=2)
#使用数据集X和y来训练KNN回归器
reg2.fit(X,y)
#绘制散点图
plt.scatter(X,y,c='b',edgecolor='k')
#绘制KNN回归器的拟合线
plt.plot(z,reg2.predict(z),c='r',linewidth=2)
#添加图表标题
plt.title('KNN Regressor')
#显示图表
plt.show()
#输出模型评分
print('模型评分：{:.2f}'.format(reg2.score(X,y)))

import numpy as np
import pandas as pd
# 读取数据集
data = pd.read_csv(r'C:\ABC\Admission_Predict.csv')
# 查看数据集前五行
data.head()
# 查看数据集信息
data.info()
# 描述性统计
data.describe()
# 重新读取数据集，并删除 'Serial No.' 列
df = pd.read_csv(r'C:\ABC\Admission_Predict.csv')
df.drop(['Serial No.'], axis=1, inplace=True)
# 将除了 'Chance of Admit ' 列以外的列作为特征变量 X，'Chance of Admit ' 列作为目标变量 y
X = df.drop(['Chance of Admit '], axis=1)
y = df['Chance of Admit '].values
# 查看处理后的数据集前五行
df.head()

from sklearn.model_selection import train_test_split
# 使用 train_test_split 函数将数据集分为训练集和测试集，并返回四个变量
# X_train: 训练集特征数据
# X_test: 测试集特征数据
# y_train: 训练集标签数据
# y_test: 测试集标签数据
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
# 输出训练集和测试集的形状信息
print('X_train shape:{}'.format(X_train.shape))
print('X_test shape:{}'.format(X_test.shape))
print('y_train shape:{}'.format(y_train.shape))
print('y_test shape:{}'.format(y_test.shape))


#导入K近邻回归算法
from sklearn.neighbors import KNeighborsRegressor
#使用默认参数进行训练
reg = KNeighborsRegressor()
reg.fit(X_train, y_train)
#打印验证数据集和训练数据集的得分
print('验证数据集得分：{:.2f}'.format(reg.score(X_test, y_test)))
print('训练数据集得分：{:.2f}'.format(reg.score(X_train, y_train)))
#使用n_neighbors=2进行训练
reg2 = KNeighborsRegressor(n_neighbors=2)
reg2.fit(X_train, y_train)
#打印模型参数n_neighbors=2的验证数据集和训练数据集的得分
print('模型参数n_neighbors=2的验证数据集得分：{:.2f}'.format(reg2.score(X_test, y_test)))
print('模型参数n_neighbors=2的训练数据集得分：{:.2f}'.format(reg2.score(X_train, y_train)))
#使用weights='distance'进行训练
reg_w = KNeighborsRegressor(weights='distance')
reg_w.fit(X_train, y_train)
#打印模型参数weights='distance'的验证数据集和训练数据集的得分
print('模型参数weights=distance的验证数据集得分：{:.2f}'.format(reg_w.score(X_test, y_test)))
print('模型参数weights=distance的训练数据集得分：{:.2f}'.format(reg_w.score(X_train, y_train)))
#打印训练后的模型
print(reg_w)

#导入MinMaxScaler数据预处理工具
from sklearn.preprocessing import MinMaxScaler
#对特征数据进行MinMaxScaler预处理，返回预处理后的X_2数据
X_2 = MinMaxScaler().fit_transform(X)
#打印预处理后的X_2
print(X_2)
#利用train_test_split函数分割数据集
#将处理后的X_2和y分割为训练集和验证集
X_train_pp, X_test_pp, y_train, y_test = train_test_split(X_2, y, random_state=0)
#构建未处理的数据集上的KNN模型，并利用训练数据进行拟合
reg_scaled = KNeighborsRegressor()
reg_scaled.fit(X_train_pp, y_train)
#打印未处理数据集的模型评分结果
print('数据预处理后的模型验证集得分：{:.2f}'.format(reg_scaled.score(X_test_pp, y_test)))
print('数据预处理后的模型训练集得分：{:.2f}'.format(reg_scaled.score(X_train_pp, y_train)))
#构造一个新的特征数据
X_new = np.array([[337, 118, 4, 4.5, 4.5, 9.65, 1]])
#利用未处理的数据集上的KNN模型进行预测
prediction = reg.predict(X_new)
print('K最近邻算法模型预测结果：')
print("预测小P同学综合评分为：{}".format(prediction))
#利用预处理后的数据集上的KNN模型进行预测
prediction = reg_scaled.predict(X_new)
print('K最近邻算法模型预测结果：')
print("预测小P同学综合评分为：{}".format(prediction))
