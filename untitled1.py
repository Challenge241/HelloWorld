# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 22:20:58 2023

@author: Lenovo
"""

import pandas as pd

# 定义一个字典类型的数据
data = {'性别':[0,0,1,1],
        '化妆':[1,0,0,0],
        '打游戏':[0,0,1,0],
        '礼物':['口红','包包','Xbox','限量版球鞋']}

# 将字典转化为Pandas的DataFrame
df = pd.DataFrame(data)

# 输出DataFrame的前五行
df.head()

from sklearn import tree

# 将礼物列从DataFrame中删除，作为特征
x = df.drop('礼物', axis=1)

# 将礼物列作为分类的目标
y = df['礼物']

# 定义决策树分类器
clf = tree.DecisionTreeClassifier()

# 训练模型
clf.fit(x, y)

# 定义一个新的样本（0代表女性，1代表男性，1代表玩游戏，0代表不化妆）
child = [0,1,0]

# 预测孩子会收到的礼物
gift = clf.predict([child])

# 输出预测结果
print(gift)

from sklearn.datasets import make_blobs

# 随机生成一组数据集，用于聚类
X, y = make_blobs(n_samples=100, centers=3, n_features=2)

# 输出数据集的形状
X.shape

import matplotlib.pyplot as plt

# 设置绘图大小
plt.figure(figsize=(9,6))

# 绘制散点图
plt.scatter(X[:,0], X[:,1], c=y, cmap='autumn', edgecolors='k', s=80)

# 显示图形
plt.show()

import numpy as np
clf1 = tree.DecisionTreeClassifier(max_depth=1)  # 创建决策树分类器，设置最大深度为1
clf1.fit(X, y)  # 训练决策树分类器
x_min, x_max = X[:, 0].min()-1, X[:, 0].max()+1  # 设置横坐标的范围
y_min, y_max = X[:, 1].min()-1, X[:, 1].max()+1  # 设置纵坐标的范围
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02), np.arange(y_min, y_max, 0.02))  # 生成网格点坐标
z = clf1.predict(np.c_[xx.ravel(), yy.ravel()])  # 预测每个网格点的标签
z = z.reshape(xx.shape)  # 重新调整形状，使之与xx、yy相同
plt.figure(figsize=(9, 6))
plt.pcolormesh(xx, yy, z, cmap='spring')  # 用颜色填充分类区域
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='autumn', edgecolor='k', s=80)  # 绘制样本点
plt.xlim(xx.min(), xx.max())  # 设置横坐标的范围
plt.ylim(yy.min(), yy.max())  # 设置纵坐标的范围
plt.title("Tree: (max_depth=1)")  # 设置图的标题
plt.show()  # 显示图像

import numpy as np
# 使用最大深度为3的决策树
clf3 = tree.DecisionTreeClassifier(max_depth=3)
# 训练模型
clf3.fit(X, y)
# 确定绘图区间
x_min, x_max = X[:,0].min() - 1, X[:,0].max() + 1
y_min, y_max = X[:,1].min() - 1, X[:,1].max() + 1
# 生成网格点
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02), np.arange(y_min, y_max, 0.02))
# 预测网格点所属的类别
z = clf3.predict(np.c_[xx.ravel(), yy.ravel()])    
z = z.reshape(xx.shape)
# 绘图
plt.figure(figsize=(9,6)) 
plt.pcolormesh(xx, yy, z, cmap='spring')
plt.scatter(X[:,0], X[:,1], c=y, cmap='autumn', edgecolor='k', s=80)
plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
plt.title("Tree: (max_depth=3)")
plt.show()

import numpy as np

# 创建深度为10的决策树分类器
clf10 = tree.DecisionTreeClassifier(max_depth=10)
clf10.fit(X, y)

# 确定画图边界
x_min, x_max = X[:,0].min() - 1, X[:,0].max() + 1
y_min, y_max = X[:,1].min() - 1, X[:,1].max() + 1

# 创建网格点坐标矩阵
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02), np.arange(y_min, y_max, 0.02))

# 在网格点上进行预测，并将预测结果转化为二维矩阵
z = clf10.predict(np.c_[xx.ravel(), yy.ravel()])    
z = z.reshape(xx.shape)

# 创建画布
plt.figure(figsize=(9,6)) 

# 绘制背景色
plt.pcolormesh(xx, yy, z, cmap='spring')

# 绘制散点图
plt.scatter(X[:,0], X[:,1], c=y, cmap='autumn', edgecolor='k', s=80)

# 设置x轴和y轴的边界
plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())

# 设置标题
plt.title("Tree: (max_depth=10)")

# 显示图形
plt.show()

# 绘制树的图形
tree.plot_tree(clf10)
plt.show()

# 导入随机森林分类器
from sklearn.ensemble import RandomForestClassifier

# 生成数据集
X,y=make_blobs(n_samples=100,centers=3,n_features=2,random_state=42)

# 创建一个随机森林分类器，并拟合数据
forest=RandomForestClassifier().fit(X,y)

# 展示随机森林分类器的相关参数
forest

# 为了绘制分类图，获取数据点最大最小值，构建网格数据
x_min,x_max=X[:,0].min()-1,X[:,0].max()+1
y_min,y_max=X[:,1].min()-1,X[:,1].max()+1
xx,yy=np.meshgrid(np.arange(x_min,x_max,0.02),
                  np.arange(y_min,y_max,0.02))

# 预测网格数据的分类结果，并将结果转化为矩阵格式
Z=forest.predict(np.c_[xx.ravel(),yy.ravel()])
Z=Z.reshape(xx.shape)

# 绘制分类图
plt.figure(figsize=(9,6)) 
plt.pcolormesh(xx,yy,Z,cmap='cool')
plt.scatter(X[:,0],X[:,1],c=y,cmap='Accent',edgecolor='k',s=80)
plt.xlim(xx.min(),xx.max())
plt.ylim(yy.min(),yy.max())
plt.title("Classifier:RandonForest")
plt.show()

# 读取心脏病数据集
heart =pd.read_csv(r"D:\2587897966\FileRecv\heart.csv")

# 展示数据集前5行
heart.head()

# 展示数据集信息，包括特征数量、数据类型等
heart.info()

# 创建一个决策树分类器
clf_tree=tree.DecisionTreeClassifier()

from sklearn.model_selection import train_test_split

# 分割数据集为训练集和测试集
x = heart.drop('target',axis=1)
y = heart['target']
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=0)

# 训练决策树模型并输出训练集和测试集的得分
clf_tree.fit(x_train, y_train)
print(clf_tree.score(x_train, y_train))
print(clf_tree.score(x_test, y_test))

score_list = []
for i in range(10, 100, 10):
    # 训练随机森林模型并记录测试集得分
    clf_forest = RandomForestClassifier(n_estimators=i, random_state=0)
    clf_forest.fit(x_train, y_train)
    score_list.append(clf_forest.score(x_test, y_test))

# 可视化不同树的数量对模型准确率的影响
plt.plot(range(10, 100, 10), score_list)
plt.show()

