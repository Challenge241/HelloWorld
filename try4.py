# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 14:51:26 2023

@author: Lenovo
"""
# 导入所需的库
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
import numpy as np
# 生成带标签的数据集，centers=4 表示生成4个聚类中心
x, y = make_blobs(centers=4, random_state=18)
# 将标签 y 取模2，实现将四类样本映射到二维空间上
y = y % 2
# 绘制散点图，x[:,0] 表示 x 的第一列数据，x[:,1] 表示 x 的第二列数据
# c=y 表示将 y 标签作为颜色，s=80 表示散点的大小，cmap='autumn' 表示颜色映射
# edgecolor='k' 表示散点边缘的颜色为黑色
plt.scatter(x[:, 0], x[:, 1], c=y, s=80, cmap='autumn', edgecolor='k')
# 显示图形
plt.show()
# 导入绘图工具包和numpy
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D, axes3d
# 创建数据
x_new = np.hstack([x, x[:, 1:]**2])  # 在原始数据的基础上添加平方项
mask = y == 0  # 用于分离出不同类别的数据点
# 创建3D图形窗口，并用scatter绘制数据点
figure = plt.figure()
ax = Axes3D(figure, elev=-152, azim=26)  # 创建3D坐标轴
ax.scatter(x_new[mask, 0], x_new[mask, 1], x_new[mask, 2], c='r', s=80)  # 绘制类别0的数据点
ax.scatter(x_new[~mask, 0], x_new[~mask, 1], x_new[~mask, 2], c='b', marker='*', s=80)  # 绘制类别1的数据点
plt.show()  # 显示图形
from sklearn.svm import LinearSVC  # 从scikit-learn中导入LinearSVC模型
linear_svm_3d = LinearSVC().fit(x_new, y)  # 训练一个LinearSVC模型
coef, intercept = linear_svm_3d.coef_.ravel(), linear_svm_3d.intercept_  # 获取模型的系数和截距
figure = plt.figure()  # 创建一个图像对象
ax = Axes3D(figure, elev=-152, azim=26)  # 创建一个3D坐标系
xx = np.linspace(x_new[:, 0].min()-2, x_new[:, 0].max()+2, 50)  # 在x轴范围内生成50个等距的点
yy = np.linspace(x_new[:, 1].min()-2, x_new[:, 1].max()+2, 50)  # 在y轴范围内生成50个等距的点
XX, YY = np.meshgrid(xx, yy)  # 生成二维网格
ZZ = (coef[0] * XX + coef[1] * YY + intercept) / -coef[2]  # 根据平面方程计算对应的z值
ax.plot_surface(XX, YY, ZZ, rstride=8, cstride=8, alpha=0.3)  # 绘制平面
ax.scatter(x_new[mask, 0], x_new[mask, 1], x_new[mask, 2], c='r', s=80)  # 绘制正样本点
ax.scatter(x_new[~mask, 0], x_new[~mask, 1], x_new[~mask, 2], c='b', marker='*', s=80)  # 绘制负样本点
plt.show()  # 显示图像

# 导入SVM模块
from sklearn import svm
# 生成二维样本数据，共50个样本，2个中心，随机种子为20
x, y = make_blobs(n_samples=50, centers=2, random_state=20)
# 创建SVM分类器，核函数为径向基函数，gamma为0.1
clf = svm.SVC(kernel='rbf', gamma=0.1)
# 使用样本数据训练分类器
clf.fit(x, y)
# 绘制样本散点图，颜色根据分类标签y的值进行区分，散点大小为80，颜色图谱为autumn，边缘颜色为gray
plt.scatter(x[:, 0], x[:, 1], c=y, s=80, cmap='autumn', edgecolor='gray')
# 获取当前坐标轴对象
ax = plt.gca()
# 获取x和y轴的取值范围
xlim = ax.get_xlim()
ylim = ax.get_ylim()
# 在x和y轴的取值范围内分别生成30个均匀分布的点，用于绘制等高线图
xx = np.linspace(xlim[0], xlim[1], 30)
yy = np.linspace(ylim[0], ylim[1], 30)
YY, XX = np.meshgrid(yy, xx)
# 将xx和yy中的点按行组合成一个二维数组
xy = np.vstack([XX.ravel(), YY.ravel()]).T
# 计算每个点到分类边界的距离
Z = clf.decision_function(xy).reshape(XX.shape)
# 绘制等高线图，用黑色显示分类边界，线条样式为虚线和实线的组合，透明度为0.5，分别绘制分类边界为-1，0，1的等高线
ax.contour(XX, YY, Z, color='k', levels=[-1, 0, 1], alpha=0.5, linestyles=['--', '-', '--'])
# 绘制SVM分类器的支持向量
ax.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[:, 1], s=100, linewidth=1, facecolors='none')
# 显示图像
plt.show()

# 导入Iris数据集
from sklearn.datasets import load_iris

# 定义生成网格点的函数
def make_meshgrid(x, y, h=.02):
    # 计算x和y轴上的最小值和最大值，并加上偏移量1
    x_min, x_max = x.min() - 1, x.max() + 1
    y_min, y_max = y.min() - 1, y.max() + 1
    # 生成网格点，h为网格点间距
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))
    return xx, yy

# 定义绘制等高线图的函数
def plot_contours(ax, clf, xx, yy, **params):
    # 对网格点进行预测
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    # 将预测结果重塑为二维数组
    Z = Z.reshape(xx.shape)
    # 绘制等高线图，填充颜色使用params中指定的颜色图谱
    out = ax.contourf(xx, yy, Z, **params)
    return out

# 导入sklearn中的load_iris函数，该函数用于载入iris数据集
from sklearn.datasets import load_iris
# 导入sklearn中的SVM分类器模型
from sklearn import svm
# 导入make_meshgrid和plot_contours函数用于可视化分类边界
from matplotlib import pyplot as plt
from mlxtend.plotting import plot_decision_regions
import numpy as np

# 载入iris数据集
iris = load_iris()
# 只选取前两个特征用于可视化
X = iris.data[:,:2]
# 目标变量
y = iris.target
# 定义SVM分类器模型的C参数值
C = 1.0
# 定义三个不同的核函数模型，包括线性核函数、径向基核函数和多项式核函数
models=(svm.SVC(kernel='linear',C=C),
        svm.SVC(kernel='rbf',gamma=0.7,C=C),
        svm.SVC(kernel='poly',degree=3,C=C))
# 对三个模型进行训练并保存
models=(clf.fit(X,y) for clf in models)
# 三个模型的标题
titles=('SVC with linear kernel',
       'SVC with RBF kernel',
       'SVC with polynomial (degree 3) kernel')
# 创建一个1行3列的图表
fig,sub=plt.subplots(1,3,figsize=(12,3))
# 调整子图之间的间距
plt.subplots_adjust(wspace=0.4,hspace=0.2)
# 用X的前两个特征的最大值和最小值定义网格，h=0.02为步长
X0,X1=X[:,0],X[:,1]
xx,yy=make_meshgrid(X0,X1)
# 对于每个模型，用plot_contours函数绘制决策边界
# 并用scatter函数绘制训练集数据点
# 最后，对图表进行设置，包括坐标轴范围，标签等等
for clf,title,ax in zip(models,titles,sub.flatten()):
    plot_contours(ax,clf,xx,yy,
                 cmap=plt.cm.autumn,alpha=0.8)
    ax.scatter(X0,X1,c=y,cmap=plt.cm.plasma,s=40,edgecolor='k')
    ax.set_xlim(xx.min(),xx.max())
    ax.set_ylim(yy.min(),yy.max())
    ax.set_xlabel('Feature 0')
    ax.set_ylabel('Feature 1')
    ax.set_xticks(())
    ax.set_yticks(())
    ax.set_title(title)
# 显示图表
plt.show()

models = (svm.SVC(kernel='rbf', gamma=0.5),
          svm.SVC(kernel='rbf', gamma=5),
          svm.SVC(kernel='rbf', gamma=50))
# 将模型拟合到数据上
models = (clf.fit(X, y) for clf in models)
titles = ('gamma=0.5',
          'gamma=5',
          'gamma=50',)
# 在3个子图中绘制决策边界和数据点
fig, sub = plt.subplots(1, 3, figsize=(10, 3))
X0, X1 = X[:, 0], X[:, 1]
xx, yy = make_meshgrid(X0, X1)
for clf, title, ax in zip(models, titles, sub.flatten()):
    # 绘制决策边界
    plot_contours(ax, clf, xx, yy, cmap=plt.cm.autumn, alpha=0.8)
    # 绘制数据点
    ax.scatter(X0, X1, c=y, cmap=plt.cm.spring, s=40, edgecolor='k')
    ax.set_xlim(xx.min(), xx.max())
    ax.set_ylim(yy.min(), yy.max())
    ax.set_xlabel('Feature 0')
    ax.set_ylabel('Feature 1')
    ax.set_xticks(())
    ax.set_yticks(())
    ax.set_title(title)
# 显示图像
plt.show()

models=(svm.SVC(kernel='rbf',C=0.01),
       svm.SVC(kernel='rbf',C=1),
       svm.SVC(kernel='rbf',C=100))
# 定义三个不同的支持向量机模型，使用RBF核函数，C分别为0.01、1、100
models=(clf2.fit(X,y) for clf2 in models)
# 在iris数据集上，分别使用三个不同的模型进行训练
titles=('C=0.01',
       'C=1',
       'C=100',)
# 定义三个不同的图表标题
fig,sub=plt.subplots(1,3,figsize=(10,3))
# 创建1行3列的子图表
X0,X1=X[:,0],X[:,1]
# 获取数据的前两个特征
xx,yy=make_meshgrid(X0,X1)
# 生成一个网格用于绘制分类区域
for clf,title,ax in zip(models,titles,sub.flatten()):
    # 对于每个模型，获取对应的标题和对应的子图表
    plot_contours(ax,clf,xx,yy,
                 cmap=plt.cm.autumn,alpha=0.8)
    # 绘制分类区域
    ax.scatter(X0,X1,c=y,cmap=plt.cm.spring,s=40,edgecolor='k')
    # 绘制样本点
    ax.set_xlim(xx.min(),xx.max())
    ax.set_ylim(yy.min(),yy.max())
    ax.set_xlabel('Feature 0')
    ax.set_ylabel('Feature 1')
    ax.set_xticks(())
    ax.set_yticks(())
    ax.set_title(title)
    # 对子图表进行设置，如横纵坐标标签、标题等
plt.show()
# 展示图表


import pandas as pd  # 导入Pandas库，用于读取和处理数据
abalone=pd.read_csv(r'D:\bays\abalone.csv')  # 使用Pandas读取数据文件
abalone.head()  # 显示数据前5行
abalone.info()  # 显示数据信息
import seaborn as sns  # 导入Seaborn库，用于数据可视化
sns.countplot(x='Sex',data=abalone,palette='Set2')  # 绘制柱状图
plt.show()  # 显示图形
abalone['age']=abalone['Rings']+1.5  # 计算年龄
plt.figure(figsize=(15,5))  # 创建一个新的图形，并设置其大小
sns.swarmplot(x='Sex',y='age',data=abalone,hue='Sex')  # 绘制散点图
sns.violinplot(x='Sex',y='age',data=abalone)  # 绘制小提琴图
plt.show()  # 显示图形


from sklearn.model_selection import train_test_split # 导入 train_test_split 模块，用于划分数据集
from sklearn.svm import SVR # 导入 SVR 模块，用于支持向量回归
data=pd.get_dummies(abalone) # 将字符串特征转换为数字编码的虚拟特征
data.head() # 显示数据框的前 5 行数据
x=data.drop(['Rings','age'],axis=1) # 获取除目标变量和辅助变量外的特征数据
y=data['age'] # 获取目标变量数据
x_train,x_test,y_train,y_test=train_test_split(x,y) # 划分训练集和测试集
x_train.shape # 显示训练集特征数据的形状
svr=SVR(gamma=0.125) # 实例化 SVR 模型，设置 gamma 参数
svr.fit(x_train,y_train) # 使用训练集数据拟合 SVR 模型
svr.score(x_test,y_test) # 使用测试集数据评估 SVR 模型的性能
data.boxplot(rot=270,figsize=(15,5)) # 绘制箱线图，可视化数据的分布情况
plt.show() # 显示箱线图
plt.scatter(x=data['Length'],y=data['age']) # 绘制散点图，展示长度特征和目标变量之间的关系
plt.grid(True) # 添加网格线
plt.show() # 显示散点图


data=data.drop(data[data['age']>25].index) # 剔除年龄大于25的数据行
data=data.drop(data[data['Length']<0.1].index) # 剔除长度小于0.1的数据行
data=data.drop(data[data['Length']>=0.8].index) # 剔除长度大于等于0.8的数据行
np.max(data.age),np.max(data.Length),np.min(data.Length) # 查看数据中age和Length列的最大值和最小值
data.drop(data[(data['Height']>0.4)&(data['age']<15)].index,inplace=True) # 剔除身高大于0.4且年龄小于15的数据行
data.drop(data[(data['Height']<0.4)&(data['age']>25)].index,inplace=True) # 剔除身高小于0.4且年龄大于25的数据行
data.drop(data[(data['Diameter']<0.1)&(data['age']<5)].index,inplace=True) # 剔除直径小于0.1且年龄小于5的数据行
data.drop(data[(data['Diameter']<0.5)&(data['age']>25)].index,inplace=True) # 剔除直径小于0.5且年龄大于25的数据行
data.drop(data[(data['Diameter']>=0.6)&(data['age']<25)].index,inplace=True) # 剔除直径大于等于0.6且年龄小于25的数据行
data.drop(data[(data['Whole weight']>=2.5)&(data['age']<25)].index,inplace=True) # 剔除整体重量大于等于2.5且年龄小于25的数据行
data.drop(data[(data['Whole weight']<2.5)&(data['age']>25)].index,inplace=True) # 剔除整体重量小于2.5且年龄大于25的数据行
data.drop(data[(data['Shucked weight']>=1)&(data['age']<20)].index,inplace=True) # 剔除去壳重量大于等于1且年龄小于20的数据行
data.drop(data[(data['Shucked weight']<1)&(data['age']>20)].index,inplace=True) # 剔除去壳重量小于1且年龄大于20的数据行
data.drop(data[(data['Shell weight']>0.6)&(data['age']<25)].index,inplace=True) # 剔除贝壳重量大于0.6且年龄小于25的数据行
data.drop(data[(data['Shell weight']<0.8)&(data['age']>25)].index,inplace=True) # 剔除贝壳重量小于0.8且年龄大于25的数据行
data.drop(data[(data['Viscera weight']>0.5)&(data['age']<20)].index,inplace=True) # 剔除内脏重量大于0.5且
data.describe()


from sklearn.preprocessing import StandardScaler  # 导入数据标准化的包
x = data.drop(['Rings', 'age'], axis=1)  # 取数据集x部分，去掉'Rings'和'age'两列
y = data['age']  # 取数据集y部分，即目标值
scaler = StandardScaler()  # 初始化标准化器
x_scld = scaler.fit_transform(x)  # 对x进行标准化
x_train_scld, x_test_scld, y_train, y_test = train_test_split(x_scld, y, random_state=888)  # 对数据进行划分，划分比例默认为0.75/0.25
svr = SVR()  # 初始化支持向量回归器
svr.fit(x_train_scld, y_train)  # 训练支持向量回归器
svr.score(x_test_scld, y_test)  # 在测试集上计算回归器的得分
