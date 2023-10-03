# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# 导入pandas库，并读取CSV文件数据
# 'D:\\LiulanqiDownload\\bank\\bank.csv' 是文件路径，sep=';' 表示CSV文件中数据项之间的分隔符是分号
data = pd.read_csv('D:\\LiulanqiDownload\\bank\\bank.csv', sep=';')
# 输出data的前5行数据
print(data.head())
# 输出data的基本信息，包括数据类型、数据总数、每列数据的非空值数量等
print(data.info())
# 输出data中数值类型数据的基本统计信息，包括总数、平均数、标准差、最小值、最大值等
print(data.describe())
# 绘制data中年龄（age）数据的分布直方图
sns.displot(x=data['age'])
plt.show()
# 绘制data中婚姻状况（marital）数据的数量统计柱状图
sns.countplot(x=data['marital'])
plt.show()
# 将data中的数据按婚姻状况（marital）分组，分别绘制每组中年龄（age）数据的分布直方图，bins=10 表示将数据分成10个区间
grid = sns.FacetGrid(data, col='marital')
grid.map(plt.hist, 'age', bins=10)
plt.show()


from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import svm
import pickle
# 导入sklearn库中的digits数据集，包含了手写数字的图像数据
digits = datasets.load_digits()
# 从digits数据集中获取手写数字图像数据
x = digits.data
# 从digits数据集中获取手写数字图像的标签
y = digits.target
# 将数据集按照一定的比例分成训练集和测试集，random_state=42 表示设置随机数种子为42，确保每次运行得到的训练集和测试集是一样的
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=42)
# 输出训练集和测试集的大小，即数据量和特征数
print(x_train.shape, x_test.shape)
# 使用SVM分类器（SVC）进行训练
clf = svm.SVC()
clf.fit(x_train, y_train)
# 输出分类器在测试集上的准确率
print(clf.score(x_test, y_test))
# 将训练好的模型保存为文件
model = open('model.pkl', 'wb')
pickle.dump(clf, model)
model.close()
# 从文件中读取保存的模型
model_file = open('model.pkl', 'rb')
clf2 = pickle.load(model_file)
# 对测试集的最后一条数据进行预测，并输出预测结果和真实结果
y_hat = clf.predict(x_test[-1:])
print(f"真实值：{y_test[-1]}", f"预测值：{y_hat}")
