# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 18:43:40 2023

@author: Lenovo
"""

from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
# 创建一个包含一个聚类中心的星形数据集
data_stars = make_blobs(random_state=11, centers=1)
# 取数据集的特征值
X_stars = data_stars[0]
# 绘制散点图
plt.scatter(X_stars[:, 0], X_stars[:, 1], c='b', marker='*')
plt.show()


from sklearn.cluster import KMeans
import numpy as np
# 创建样本数据
data_stars = make_blobs(random_state=11, centers=1)
X_stars = data_stars[0]
# 创建KMeans对象
kmeans = KMeans(n_clusters=4)
# 训练KMeans模型
kmeans.fit(X_stars)
# 定义图像显示的x轴、y轴的范围
x_min, x_max = X_stars[:, 0].min() - 0.5, X_stars[:, 0].max() + 0.5
y_min, y_max = X_stars[:, 1].min() - 0.5, X_stars[:, 1].max() + 0.5
# 生成网格点坐标矩阵
xx, yy = np.meshgrid(np.arange(x_min, x_max, .02), np.arange(y_min, y_max, .02))
# 预测网格点所属的类别
Z = kmeans.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
# 创建子图1并显示网格点聚类结果
plt.figure(1)
plt.clf()
plt.imshow(Z, interpolation='nearest',
           extent=(xx.min(), xx.max(), yy.min(), yy.max()),
           cmap=plt.cm.Pastel2,
           aspect='auto', origin='lower')
plt.plot(X_stars[:, 0], X_stars[:, 1], 'r.', markersize=6, marker='*', c='b')
centroids = kmeans.cluster_centers_
plt.scatter(centroids[:, 0], centroids[:, 1],
            marker='*', s=150, linewidths=3,
            color='r', zorder=10)
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(())
plt.yticks(())
plt.show()
# 打印聚类标签
print("K均值的聚类标签:\n{}".format(kmeans.labels_))


import matplotlib.pyplot as plt
from sklearn import datasets
import matplotlib.colors
# 创建画布
fig = plt.figure(figsize=(10, 5))
# 生成 make_circles 数据集
X_cir, y_cir = datasets.make_circles(n_samples=500, factor=.6, noise=0.05, random_state=42)
# 绘制散点图
plt.scatter(X_cir[:, 0], X_cir[:, 1], marker="o", c='g', s=60, edgecolor='k')
plt.title("make_circles Datasets")  # 添加标题
plt.xlabel("Feature 0")  # 添加横轴标签
plt.ylabel("Feature 1")  # 添加纵轴标签
plt.show()  # 显示图形

from sklearn.cluster import DBSCAN  # 导入DBSCAN算法
db = DBSCAN()  # 创建DBSCAN对象
cluster = db.fit_predict(X_cir)  # 对数据进行聚类
plt.scatter(X_cir[:,0], X_cir[:,1], marker="o", c=cluster, s=60, edgecolor='k', cmap=plt.cm.cool)  # 绘制散点图，按照类别进行不同颜色的标记
plt.title("DBSCAN Cluster")  # 设置图像标题
plt.xlabel("Feature 0")  # 设置x轴标签
plt.ylabel("Feature 1")  # 设置y轴标签
plt.show()  # 显示图像


# 导入DBSCAN算法模块
from sklearn.cluster import DBSCAN
# 构建DBSCAN模型，不指定eps参数
db = DBSCAN()
# 用DBSCAN模型拟合数据并进行聚类
cluster = db.fit_predict(X_cir)
# 绘制散点图，其中聚类结果作为颜色标签
plt.scatter(X_cir[:,0], X_cir[:,1], marker="o", c=cluster, s=60, edgecolor='k', cmap=plt.cm.cool)
# 添加标题和坐标轴标签
plt.title("DBSCAN Cluster")
plt.xlabel("Feature 0")
plt.ylabel("Feature 1")
# 显示绘制的图形
plt.show()
# 打印DBSCAN聚类(eps=0.12)的标签
print('\n\n\nDBSCAN聚类(eps=0.12)的标签为:\n{}\n\n\n'.format(cluster_eps))

from sklearn.cluster import DBSCAN
# 创建一个DBSCAN对象
db_1 = DBSCAN(min_samples=103)
# 运行聚类算法并预测每个数据点所属的簇
cluster_1 = db_1.fit_predict(X_cir)
# 用散点图展示数据点，每个数据点的颜色表示其所属的簇
plt.scatter(X_cir[:,0], X_cir[:,1], marker="o", c=cluster_1, s=60, edgecolor='k', cmap=plt.cm.cool)
plt.title("DBSCAN Cluster(min_samples=103)")
plt.xlabel("Feature 0")
plt.ylabel("Feature 1")
plt.show()


# 导入DBSCAN模型
from sklearn.cluster import DBSCAN
# 初始化DBSCAN模型，并设置eps和min_samples参数
db_2 = DBSCAN(eps=0.15, min_samples=18)
# 将模型应用于数据集并进行聚类
cluster_2 = db_2.fit_predict(X_cir)
# 绘制散点图，用聚类结果着色
plt.scatter(X_cir[:,0], X_cir[:,1], marker="o", c=cluster_2, s=60, edgecolor='k', cmap=plt.cm.cool)
# 设置图标题和坐标轴标签
plt.title("DBSCAN Cluster(eps=0.15,min_samples=18)")
plt.xlabel("Feature 0")
plt.ylabel("Feature 1")
# 显示图形
plt.show()

import pandas as pd

# 读取csv文件并存入dataframe对象data
data=pd.read_csv(r"D:\CSV\mall_customers.csv")
# 打印data的前5行数据
data.head()
# 打印data的行列数
data.shape
# 对data的数值型列进行描述性统计，并打印结果
data.describe()
# 对data中的'gender'列进行描述性统计，并打印结果
data['gender'].describe()


# 导入所需的库和模块
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
# 选择需要进行聚类的特征
X1=data[['age','spending_score']].iloc[:,:].values
# 创建一个空列表来存储每个聚类数量下的惯性
inertia=[]
# 针对不同的聚类数量进行聚类，并计算每个聚类数量下的惯性
for n in range(1,11):
    algorithm=(KMeans(n_clusters=n,init='k-means++',n_init=10,max_iter=300,
                     tol=0.0001,random_state=111,algorithm='elkan'))
    algorithm.fit(X1)
    inertia.append(algorithm.inertia_)
# 绘制每个聚类数量下的惯性折线图
plt.figure(1,figsize=(15,6))
plt.plot(np.arange(1,11),inertia,'o') # 绘制散点图
plt.plot(np.arange(1,11),inertia,'-',alpha=0.5) # 绘制折线图
plt.xlabel('Number of Clusters',fontsize=14) # x轴标签
plt.ylabel('Inertia',fontsize=14) # y轴标签
plt.show()


algorithm=(KMeans(n_clusters=4,init='k-means++',n_init=10,max_iter=300,
                  tol=0.0001,random_state=111,algorithm='elkan'))  # 初始化KMeans模型
algorithm.fit(X1)  # 训练KMeans模型
labels1=algorithm.labels_  # 模型预测的标签
centroids1=algorithm.cluster_centers_  # 模型预测的聚类中心
h=0.02
x_min,x_max=X1[:,0].min()-1,X1[:,0].max()+1
y_min,y_max=X1[:,1].min()-1,X1[:,1].max()+1
xx,yy=np.meshgrid(np.arange(x_min,x_max,h),np.arange(y_min,y_max,h))  # 生成网格点
Z=algorithm.predict(np.c_[xx.ravel(),yy.ravel()])  # 对网格点进行预测
plt.figure(1,figsize=(15,7))
plt.clf()
Z=Z.reshape(xx.shape)
plt.imshow(Z,interpolation='nearest',  # 显示聚类边界
           extent=(xx.min(),xx.max(),yy.min(),yy.max()),
           cmap=plt.cm.Pastel2,aspect='auto',origin='lower')
plt.scatter(x='age',y='spending_score',data=data,c=labels1,s=200)  # 显示散点图
plt.scatter(x=centroids1[:,0],y=centroids1[:,1],
            s=300,c='red',alpha=0.5,marker='*',linewidths=3)  # 显示聚类中心
plt.ylabel('Spending Score(1-100)',fontsize=20),plt.xlabel('Age',fontsize=20)  # 添加x、y轴标签
plt.show()  # 显示图形

X2=data[['annual_income','spending_score']].iloc[:,:].values  # 取数据中 'annual_income' 和 'spending_score' 两列数据，构成二维数组
inertia=[]  # 创建空列表，存储每个聚类数下算法的损失函数值
for n in range(1,11):
    algorithm=(KMeans(n_clusters=n,init='k-means++',n_init=10,max_iter=300,
                     tol=0.0001,random_state=111,algorithm='elkan'))  # 构建 KMeans 模型，选择 'elkan' 算法
    algorithm.fit(X2)  # 用数据拟合模型
    inertia.append(algorithm.inertia_)  # 计算并存储该聚类数下算法的损失函数值
plt.figure(1,figsize=(15,6))
plt.plot(np.arange(1,11),inertia,'o')  # 绘制损失函数随聚类数变化的图像，使用圆圈表示每个聚类数下算法的损失函数值
plt.plot(np.arange(1,11),inertia,'-',alpha=0.5)  # 连接每个圆圈
plt.xlabel('Number of Clusters'),plt.ylabel('Inertia')  # 设置横轴和纵轴标签
plt.show()  # 显示图像

# 选取 'annual_income' 和 'spending_score' 两个特征作为聚类依据，存入变量 X2
X2=data[['annual_income','spending_score']].iloc[:,:].values
# 初始化一个空列表，用来存储不同聚类数下的SSE
inertia=[]
for n in range(1,11):
    # 初始化 KMeans 聚类器，n_clusters 表示要聚类成几类
    algorithm=(KMeans(n_clusters=n,init='k-means++',n_init=10,max_iter=300,
                     tol=0.0001,random_state=111,algorithm='elkan'))
    # 对数据 X2 进行聚类
    algorithm.fit(X2)
    # 将当前聚类数下的 SSE 存入 inertia 列表中
    inertia.append(algorithm.inertia_)
# 绘制不同聚类数下的 SSE 的曲线
plt.figure(1,figsize=(15,6))
plt.plot(np.arange(1,11),inertia,'o')
plt.plot(np.arange(1,11),inertia,'-',alpha=0.5)
plt.xlabel('Number of Clusters'),plt.ylabel('Inertia')
plt.show()
# 使用聚类数为 5 的 KMeans 聚类器进行聚类
algorithm=(KMeans(n_clusters=5,init='k-means++',n_init=10,max_iter=300,
                     tol=0.0001,random_state=111,algorithm='elkan'))
algorithm.fit(X2)
# 获取聚类结果的标签和聚类中心点坐标
labels1=algorithm.labels_
centroids1=algorithm.cluster_centers_
# 为绘制分类边界做准备
h=0.02
x_min,x_max=X2[:,0].min()-1,X2[:,0].max()+1
y_min,y_max=X2[:,1].min()-1,X2[:,1].max()+1
xx,yy=np.meshgrid(np.arange(x_min,x_max,h),np.arange(y_min,y_max,h))
Z2=algorithm.predict(np.c_[xx.ravel(),yy.ravel()])
# 绘制分类边界
plt.figure(1,figsize=(15,7))
plt.clf()
Z2=Z2.reshape(xx.shape)
plt.imshow(Z2,interpolation='nearest',
          extent=(xx.min(),xx.max(),yy.min(),yy.max()),
           cmap=plt.cm.Pastel2,aspect='auto',origin='lower')
# 绘制样本点，并使用标签对样本点进行颜色分类
plt.scatter(x='annual_income',y='spending_score',data=data,c=labels1,s=200)
# 绘制聚类中心点
plt.scatter(x=centroids1[:,0],y=centroids1[:,1],
           s=300,c='red',alpha=0.5,marker='*',linewidths=3)
plt.ylabel('Spending Score(1-100)',fontsize=20)
plt.xlabel('Annual Income (k$)',fontsize=20)
plt.show()

