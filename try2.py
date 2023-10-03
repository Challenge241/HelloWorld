# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 16:40:01 2023

@author: Lenovo
"""

# 导入 numpy 和 matplotlib.pyplot 库
import numpy as np
import matplotlib.pyplot as plt
'''
# 生成 200 个均匀分布在 -10 到 10 之间的数作为自变量 x
x = np.linspace(-10, 10, 200)
# 使用简单的线性模型计算因变量 y 的值，其中斜率为 -2，截距为 3
y = -2 * x + 3
# 使用 matplotlib.pyplot 库的 plot 函数绘制线性模型图形，颜色为紫色
plt.plot(x, y, c='purple')
# 设置图形标题
plt.title('basic linear model')
# 显示图形
plt.show()
'''

# 导入 pandas、sklearn.linear_model 和 matplotlib.pyplot 库
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
# 定义数据字典，包含两个特征 Age 和 Height
data = {'Age': [14, 18], 'Height': [165, 175]}
# 使用 pandas 的 DataFrame 函数将数据字典转换为数据框
data_frame = pd.DataFrame(data)
# 打印数据框的前五行数据
print(data_frame.head())
# 创建线性回归模型
reg = LinearRegression()
# 将自变量 Age 保存在变量 x 中，并进行 reshape 操作
print("data_frame['Age']:")
print(data_frame['Age'])
x = data_frame['Age'].values.reshape(-1, 1)
print("x:")
print(x)
# 将因变量 Height 保存在变量 y 中
y = data_frame['Height']
# 使用线性回归模型拟合数据
reg.fit(x, y)
# 打印模型的斜率和截距
print(reg.coef_, reg.intercept_)

# 生成 20 个均匀分布在 10 到 20 之间的数作为自变量 z
z = np.linspace(10, 20, 20)
# 使用 matplotlib.pyplot 库的 scatter 函数绘制散点图，标记大小为 80
plt.scatter(x, y, s=80)
# 使用 matplotlib.pyplot 库的 plot 函数绘制回归线，颜色为黑色
plt.plot(z, reg.predict(z.reshape(-1, 1)), c='k')

# 设置图形标题
plt.title('Age and Height')
# 显示图形
plt.show()


# 导入必要的模块
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt
# 生成数据
z = np.linspace(10,20,20)
data2 = {'Age': [14, 16, 18], 'Height': [165, 166, 175]}
data_frame2 = pd.DataFrame(data2)
# 展示数据前几行
data_frame2.head()
# 创建线性回归模型
reg2 = LinearRegression()
x2 = data_frame2['Age'].values.reshape(-1,1)
y2 = data_frame2['Height']
reg2.fit(x2, y2)
# 绘制散点图和回归线
plt.scatter(x2, y2, s=80)
plt.plot(z, reg2.predict(z.reshape(-1,1)), c='k')
plt.title('Age and Height')
plt.show()
# 输出回归系数和截距
print(reg2.coef_, reg2.intercept_)



from sklearn.linear_model import Ridge  # 导入Ridge回归模型
import pandas as pd  # 导入pandas库，用于数据处理
from sklearn.linear_model import LinearRegression  # 导入线性回归模型
import numpy as np  # 导入numpy库，用于科学计算
import matplotlib.pyplot as plt  # 导入matplotlib库，用于数据可视化
z = np.linspace(10, 20, 20)  # 生成一个长度为20的数组，取值范围为[10, 20]
data2 = {'Age': [14, 16, 18], 'Height': [165, 166, 175]}  # 创建一个字典类型的数据
data_frame2 = pd.DataFrame(data2)  # 将字典类型的数据转化为数据框
data_frame2.head()  # 显示数据框的前几行数据
reg2 = LinearRegression()  # 创建一个线性回归模型的实例
x2 = data_frame2['Age'].values.reshape(-1, 1)  # 取出数据框中的Age列，并将其转化为二维数组
y2 = data_frame2['Height']  # 取出数据框中的Height列
ridge = Ridge().fit(x2, y2)  # 创建一个Ridge回归模型的实例，并对模型进行拟合
plt.scatter(x2, y2, s=80)  # 绘制散点图
plt.plot(z, ridge.predict(z.reshape(-1, 1)), c='k')  # 绘制Ridge回归的拟合曲线
plt.title('Age and Height')  # 添加标题
plt.show()  # 显示图像
ridge2 = Ridge(alpha=20).fit(x2, y2)  # 创建一个alpha=20的Ridge回归模型的实例，并对模型进行拟合
plt.scatter(x2, y2, s=80)  # 绘制散点图
plt.plot(z, ridge2.predict(z.reshape(-1, 1)), c='k')  # 绘制Ridge回归的拟合曲线
plt.title('Age and Height')  # 添加标题
plt.show()  # 显示图像


from sklearn.linear_model import Ridge   # 导入岭回归模型
import matplotlib.pyplot as plt   # 导入可视化模块
from sklearn.datasets import load_diabetes   # 导入糖尿病数据集
from sklearn.model_selection import train_test_split   # 导入数据集分割工具
# 导入数据集并分割成训练集和测试集
X, y = load_diabetes().data, load_diabetes().target
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=8)
# 输出训练集和数据集的形状
print(X.shape, X_train.shape)
# 对训练集数据进行岭回归拟合
ridge = Ridge(alpha=0.1).fit(X_train, y_train)
# 输出模型在训练集和测试集上的评分
print(ridge.score(X_train, y_train))
print(ridge.score(X_test, y_test))
# 在不同的 alpha 值下分别对模型进行拟合并输出评分
ridge5 = Ridge(alpha=5)
ridge5.fit(X_train, y_train)
print(ridge5.score(X_train, y_train))
print(ridge5.score(X_test, y_test))
ridge01 = Ridge(alpha=0.1).fit(X_train, y_train)
ridge1 = Ridge(alpha=1).fit(X_train, y_train)
ridge5 = Ridge(alpha=5).fit(X_train, y_train)
ridge10 = Ridge(alpha=10).fit(X_train, y_train)
# 对不同 alpha 值下的回归系数进行可视化
plt.plot(ridge01.coef_, 's', label='Ridge alpha=0.1')
plt.plot(ridge1.coef_, '-', label='Ridge alpha=1')
plt.plot(ridge5.coef_, 'v', label='Ridge alpha=5')
plt.plot(ridge10.coef_, 'o', label='Ridge alpha=10')
plt.xlabel("coefficient index")
plt.ylabel("coefficient magnitude")
plt.hlines(0, 0, len(ridge01.coef_))
plt.legend(loc='best')
plt.show()

from sklearn.linear_model import Lasso
import matplotlib.pyplot as plt # 导入绘图库
from sklearn.datasets import load_diabetes # 导入糖尿病数据集
from sklearn.model_selection import train_test_split # 导入数据集划分函数
import numpy as np # 导入数值计算库
X, y = load_diabetes().data, load_diabetes().target # 加载糖尿病数据集的特征变量和目标变量
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=8) # 对数据集进行划分，用于训练和测试
lasso = Lasso().fit(X_train, y_train) # 构建Lasso模型，对数据集进行训练
print(lasso.score(X_train, y_train)) # 输出训练集上的得分
print(lasso.score(X_test, y_test)) # 输出测试集上的得分
print(np.sum(lasso.coef_ != 0)) # 输出系数不为0的数量
lasso01 = Lasso(alpha=0.1, max_iter=100000).fit(X_train, y_train) # 构建Lasso模型，对数据集进行训练
print(lasso01.score(X_train, y_train)) # 输出训练集上的得分
print(lasso01.score(X_test, y_test)) # 输出测试集上的得分
print(np.sum(lasso01.coef_ != 0)) # 输出系数不为0的数量
lasso001 = Lasso(alpha=0.01, max_iter=100000).fit(X_train, y_train) # 构建Lasso模型，对数据集进行训练
# 绘制三个Lasso模型的系数图
plt.plot(lasso.coef_, 's', label="Lasso alpha=1") # alpha=1的系数图
plt.plot(lasso01.coef_, '-', label="Lasso alpha=0.1") # alpha=0.1的系数图
plt.plot(lasso001.coef_, 'v', label="Lasso alpha=0.01") # alpha=0.01的系数图
plt.hlines(0, 0, len(lasso.coef_)) # 添加水平线
plt.legend(ncol=2, loc=(0, 1.05)) # 添加图例，指定位置
plt.xlabel("coefficient index") # 添加x轴标签
plt.ylabel("coefficient magnitude") # 添加y轴标签
plt.show() # 显示图像


import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
# 创建一个数据框
data={'Age':[14,16,18],
      'Height':[165,163,175],
      'is_tall':[1,0,1]}
data_frame=pd.DataFrame(data)
# 查看数据框前5行数据
data_frame.head()
# 实例化Logistic回归模型
clf=LogisticRegression()
# 获取特征数据
x=data_frame.drop('is_tall',axis=1)
# 获取标签数据
y=data['is_tall']
# 将特征数据和标签数据传入模型进行拟合
clf.fit(x,y)
# 新建一组数据
student4=[[19,176]]
# 预测新数据
clf.predict(student4)
# 实例化线性支持向量机分类器
svc=LinearSVC()
# 将特征数据和标签数据传入模型进行拟合
svc.fit(x,y)
# 预测新数据
svc.predict(student4)


