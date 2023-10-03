# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 16:05:16 2023

@author: Lenovo
"""
import pandas as pd
#定义一个字典，用于存储数据
data_csv={
'年份':[2014,2015,2016,2017,2018],
'M2同比增长超过10%':[1,1,1,0,0],
'土地供应量增长超过10%':[0,0,0,1,1],
'人口是否净流入':[1,1,1,0,0],
'次年房价是否大幅上涨':[0,1,1,0,0]
}

#将字典转换成数据框
data=pd.DataFrame(data_csv)

#输出数据框前5行
data.head()

#导入BernoulliNB朴素贝叶斯分类器
from sklearn.naive_bayes import BernoulliNB

#从数据框中分离特征和标签
x=data.drop(['年份','次年房价是否大幅上涨'],axis=1)
y=data['次年房价是否大幅上涨']

#创建一个BernoulliNB分类器
clf=BernoulliNB()

#训练分类器
clf.fit(x,y)

#使用训练好的分类器进行预测，并输出准确率
clf.score(x,y)

#构造新的特征向量进行预测
x_2019=[[0,1,0]]
y_2020=clf.predict(x_2019)

#输出预测结果
print(y_2020)
# 导入需要使用的库和函数
from sklearn.datasets import make_blobs   # 用于生成聚类数据的函数
from sklearn.model_selection import train_test_split  # 用于划分训练集和测试集的函数
from sklearn.naive_bayes import BernoulliNB   # 伯努利朴素贝叶斯分类器

# 使用make_blobs函数生成400个样本，分为4类
X, y = make_blobs(n_samples=400, centers=4, random_state=8)

# 将数据集划分为训练集和测试集
# random_state参数指定划分方式，可以保证结果的可重复性
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=8)

# 定义一个伯努利朴素贝叶斯分类器
nb = BernoulliNB()

# 使用训练集对分类器进行训练
nb.fit(X_train, y_train)

# 输出模型在测试集上的得分，保留三位小数
print('模型得分:{:.3f}'.format(nb.score(X_test, y_test)))

# 导入需要使用的库和函数
import numpy as np   # 数学计算库
import matplotlib.pyplot as plt   # 可视化库

# 根据数据的范围，确定可视化的x轴和y轴的范围
x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5

# 生成网格点坐标矩阵
xx, yy = np.meshgrid(np.arange(x_min, x_max, .2),
                     np.arange(y_min, y_max, .2))

# 对网格点进行预测，并将预测结果转化为网格矩阵的形式
z = nb.predict(np.c_[(xx.ravel(), yy.ravel())]).reshape(xx.shape)

# 绘制预测结果的背景色
plt.pcolormesh(xx, yy, z, cmap=plt.cm.Pastel1)

# 绘制数据点的散点图
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Pastel2, edgecolor='k')

# 设置x轴和y轴的范围
plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())

# 设置图表的标题
plt.title('BernoulliNB')

# 显示图表
plt.show()

# 导入需要使用的库和函数
from sklearn.naive_bayes import GaussianNB   # 高斯朴素贝叶斯分类器

# 定义一个高斯朴素贝叶斯分类器
gnb = GaussianNB()

# 使用训练集对分类器进行训练
gnb.fit(X_train, y_train)

# 输出模型在测试集上的得分，保留三位小数
print('模型得分:{:.3f}'.format(gnb.score(X_test, y_test)))

# 对网格点进行预测，并将预测结果转化为网格矩阵的形式
z_gnb = gnb.predict(np.c_[(xx.ravel(), yy.ravel())]).reshape(xx.shape)

# 绘制预测结果的背景色
plt.pcolormesh(xx, yy, z_gnb, cmap=plt.cm.Pastel1)

# 绘制数据点的散点图
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Pastel2, edgecolor='k')

# 设置x轴和y轴的范围
plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())

# 设置图表的标题
plt.title('GaussianNB')

# 显示图表
plt.show()


# 导入需要使用的库和函数
from sklearn.model_selection import train_test_split   # 划分训练集和测试集的函数
import pandas as pd   # 数据处理库

# 读取数据集，数据集的路径为 D:\CSV\mushroom-csv-data-main\mushrooms.csv
mushroom = pd.read_csv(r'D:\CSV\mushroom-csv-data-main\mushrooms.csv')

# 查看数据集的前五行
mushroom.head()

# 检查数据集是否存在缺失值，并返回每列缺失值的数量
mushroom.isnull().sum()

# 查看分类变量 'class' 的取值
mushroom['class'].unique()


# 导入需要使用的库和函数
from sklearn.preprocessing import LabelEncoder   # 标签编码函数
import pandas as pd   # 数据处理库

# 创建一个标签编码器对象
labelencoder = LabelEncoder()

# 循环遍历数据集的每一列，对每一列进行标签编码
for col in mushroom.columns:
    mushroom[col] = labelencoder.fit_transform(mushroom[col])

# 查看经过标签编码后的数据集的前五行
mushroom.head()

# 使用 groupby() 函数对 'class' 列的值进行分组统计，并输出每个类别的数量
print(mushroom.groupby('class').size())

# 使用 value_counts() 函数对 'class' 列的值进行计数，并按数量降序排列
print(mushroom['class'].value_counts())

# 导入需要使用的库和函数
from sklearn.naive_bayes import MultinomialNB   # 多项式朴素贝叶斯分类器
from sklearn.model_selection import train_test_split   # 划分训练集和测试集的函数
import pandas as pd   # 数据处理库

# 从数据集中选取自变量和因变量
X = mushroom.iloc[:, 1:23]   # 自变量
y = mushroom.iloc[:, 0]   # 因变量

# 使用 train_test_split() 函数将数据集划分为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

# 创建一个多项式朴素贝叶斯分类器对象并进行训练
mnb = MultinomialNB()
mnb.fit(X_train, y_train)

# 输出多项式朴素贝叶斯分类器在训练集上的准确率
print(mnb.score(X_train, y_train))

# 输出多项式朴素贝叶斯分类器在测试集上的准确率
print(mnb.score(X_test, y_test))


from sklearn.model_selection import learning_curve
from sklearn.model_selection import ShuffleSplit

# 定义函数绘制学习曲线
def plot_learning_curve(estimator, title, X, y, ylim=None, cv=None,
                         n_jobs=-1, train_sizes=np.linspace(.1, 1.0, 5)):
    plt.figure()
    plt.title(title)
    if ylim is not None:
        plt.ylim(*ylim)
    plt.xlabel("Training examples")
    plt.ylabel("Score")
    # 使用learning_curve函数计算训练得分和验证得分
    train_sizes, train_scores, test_scores = learning_curve(
        estimator, X, y, cv=cv, n_jobs=n_jobs, train_sizes=train_sizes)
    # 计算平均训练得分和平均验证得分
    train_scores_mean = np.mean(train_scores, axis=1)
    test_scores_mean = np.mean(test_scores, axis=1)
    # 绘制图像
    plt.grid()
    plt.plot(train_sizes, train_scores_mean, 'o-', color='r',
             label='Training score')
    plt.plot(train_sizes, test_scores_mean, 'o-', color='g',
             label='Cross validation score')
    plt.legend(loc='lower right')
    return plt

# 定义交叉验证的方法
cv = ShuffleSplit(n_splits=30, test_size=0.3, random_state=28)
# 定义分类器
estimators = [MultinomialNB(), GaussianNB()]

# 对每个分类器绘制学习曲线
for estimator in estimators:
    title = estimator
    # 调用plot_learning_curve函数绘制学习曲线
    plot_learning_curve(estimator, title, X, y, ylim=(0.5, 1.0), cv=cv, n_jobs=-1)

# 显示图像
plt.show()
