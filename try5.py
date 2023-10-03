# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 15:25:19 2023

@author: Lenovo
"""
import numpy as np             # 导入NumPy库
import matplotlib.pyplot as plt   # 导入Matplotlib库
# 生成一组从-2到2的等差数列，共100个元素
line = np.linspace(-2, 2, 100)
# 用线性方程 y=max(x,0) 绘制ReLU函数的图像，线条采用点划线样式，标签为'relu'
plt.plot(line, np.maximum(line, 0), label='relu', linestyle="-.")
# 用双曲正切函数 y=tanh(x) 绘制Tanh函数的图像，线条采用虚线样式，标签为'tanh'
plt.plot(line, np.tanh(line), label='tanh', linestyle="--")
# 在最佳位置添加图例
plt.legend(loc='best')
# 添加X轴和Y轴的标签
plt.xlabel('x')
plt.ylabel('tanh(x) and relu(x)')
# 显示绘制的图像
plt.show()
from sklearn.neural_network import MLPClassifier   # 导入MLPClassifier类
import pandas as pd    # 导入Pandas库
from sklearn.datasets import load_iris  # 导入load_iris函数
from sklearn.model_selection import train_test_split   # 导入train_test_split函数
# 加载Iris数据集
iris = load_iris()
# 选取前两个特征作为输入特征
X = iris.data[:, :2]
# 将鸢尾花的类别作为标签
y = iris.target
# 将数据集分为训练集和测试集，random_state设置随机种子以保证每次运行结果一致
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
# 构建一个MLPClassifier类的实例，使用lbfgs算法进行训练
mlp = MLPClassifier(solver='lbfgs')
# 对训练集进行拟合
mlp.fit(X_train, y_train)
# 导入matplotlib库中的pyplot模块以及ListedColormap类
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
# 创建两种颜色映射
cmap_light = ListedColormap(['#FFAFAA', '#AAFFDA', '#FAAAFF'])
cmap_bold = ListedColormap(['#FF00AA', '#00FF0A', '#0FA0FF'])
# 设置x和y轴的范围
x_min, x_max = X_train[:, 0].min() - 1, X_train[:, 0].max() + 1
y_min, y_max = X_train[:, 1].min() - 1, X_train[:, 1].max() + 1
# 生成一个网格，以便在二维空间中绘制分类边界
xx, yy = np.meshgrid(np.arange(x_min, x_max, .02),
                     np.arange(y_min, y_max, .02))
# 在网格上使用模型进行预测
Z = mlp.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
# 创建一个新的图形
plt.figure()
# 使用颜色映射显示预测结果
plt.pcolormesh(xx, yy, Z, cmap=cmap_light)
# 绘制数据点并使用真实标签着色
plt.scatter(X[:, 0], X[:, 1], c=y, edgecolor='k', s=60)
# 设置x轴和y轴的范围
plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
# 设置图形的标题
plt.title("MLPClassifier:solver=lbfgs")
# 显示图形
plt.show()
# 输出模型在训练集上的得分
print('MLPClassifier:solver=lbfgs 得分：{:.2f}%,'.format(mlp.score(X_train, y_train) * 100))

# 导入MLPClassifier类和绘图相关的库
from sklearn.neural_network import MLPClassifier
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

# 定义两种颜色映射
cmap_light=ListedColormap(['#FFAFAA','#AAFFDA','#FAAAFF'])
cmap_bold=ListedColormap(['#FF00AA','#00FF0A','#0FA0FF'])

# 构建单层神经网络分类器，使用lbfgs作为优化算法，有20个隐藏层节点，然后用训练集进行训练
mlp_20=MLPClassifier(solver='lbfgs',hidden_layer_sizes=[20])
mlp_20.fit(X_train,y_train)

# 用网格图对所有点进行预测，并重新调整形状
Z1=mlp_20.predict(np.c_[xx.ravel(),yy.ravel()])
Z1=Z1.reshape(xx.shape)

# 创建画布并绘制预测的分类边界和训练集样本点
plt.figure()
plt.pcolormesh(xx,yy,Z1,cmap=cmap_light)
plt.scatter(X[:,0],X[:,1],c=y,edgecolor='k',s=60)
plt.xlim(xx.min(),xx.max())
plt.ylim(y.min(),yy.max())
plt.title('MLPClassifier:nodes=20')
plt.show()

# 构建两层神经网络分类器，使用lbfgs作为优化算法，每层有20个隐藏层节点，然后用训练集进行训练
mlp_2L=MLPClassifier(solver='lbfgs',hidden_layer_sizes=[20,20])
mlp_2L.fit(X_train,y_train)

# 用网格图对所有点进行预测，并重新调整形状
Z1=mlp_2L.predict(np.c_[xx.ravel(),yy.ravel()])
Z1=Z1.reshape(xx.shape)

# 创建画布并绘制预测的分类边界和训练集样本点
plt.figure()
plt.pcolormesh(xx,yy,Z1,cmap=cmap_light)
plt.scatter(X[:,0],X[:,1],c=y,edgecolor='k',s=60)
plt.xlim(xx.min(),xx.max())
plt.ylim(y.min(),yy.max())
plt.title('MLPClassifier:2layers')
plt.show()

# 创建MLP分类器，使用lbfgs求解器和20个隐藏节点
mlp_tanh = MLPClassifier(solver='lbfgs', hidden_layer_sizes=[20], activation='tanh')
# 使用训练数据拟合MLP分类器
mlp_tanh.fit(X_train, y_train)
# 对网格点进行预测
Z2 = mlp_tanh.predict(np.c_[xx.ravel(), yy.ravel()])
# 对预测结果进行重塑
Z2 = Z2.reshape(xx.shape)
# 创建一个新的图形
plt.figure()
# 绘制网格点的分类结果
plt.pcolormesh(xx, yy, Z2, cmap=cmap_light)
# 绘制训练集样本点
plt.scatter(X[:, 0], X[:, 1], c=y, edgecolor='k', s=60)
# 设置坐标轴范围
plt.xlim(xx.min(), xx.max())
plt.ylim(y.min(), yy.max())
# 设置图形标题
plt.title('MLPClassifier:2layers with tanh')
# 显示图形
plt.show()

# 创建MLP分类器，使用lbfgs求解器、20个隐藏节点、tanh激活函数和alpha值为1
mlp_tanh = MLPClassifier(solver='lbfgs', hidden_layer_sizes=[20], activation='tanh', alpha=1)
# 使用训练数据拟合MLP分类器
mlp_tanh.fit(X_train, y_train)
# 对网格点进行预测
Z3 = mlp_tanh.predict(np.c_[xx.ravel(), yy.ravel()])
# 对预测结果进行重塑
Z3 = Z3.reshape(xx.shape)
# 创建一个新的图形
plt.figure()
# 绘制网格点的分类结果
plt.pcolormesh(xx, yy, Z3, cmap=cmap_light)
# 绘制训练集样本点
plt.scatter(X[:, 0], X[:, 1], c=y, edgecolor='k', s=60)
# 设置坐标轴范围
plt.xlim(xx.min(), xx.max())
plt.ylim(y.min(), yy.max())
# 设置图形标题
plt.title('MLPClassifier:alpha=1')
# 显示图形
plt.show()

import pandas as pd 
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split

# 从CSV文件中读取数据
data = pd.read_csv(r'C:\ABC\fashion-mnist_test.csv',sep=',')
data.keys()

# 提取输入和输出变量
X = data.drop(['label'],axis=1)
y = data['label']

# 将数据集分割为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(
    X, y, train_size=6000, test_size=1200, random_state=42)

# 对输入数据进行归一化处理
X_train = X_train/255.
X_test = X_test/255.

# 训练数据对应的类别列表
class_t = [
    "0：T-shirt/top",
    "1：Trouser",
    "2：Pullover",
    "3：Dress",
    "4：Coat",
    "5：Sandal",
    "6：Shirt",
    "7：Sneaker",
    "8：Bag",
    "9：Ankle boot",
]

# 获取对应类别的标签
def get_label_class(label):
    return class_t[label]

# 输出标签为4的类别
get_label_class(4)


