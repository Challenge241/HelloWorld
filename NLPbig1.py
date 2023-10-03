# -*- coding: utf-8 -*-
"""
Created on Sun May  7 20:26:31 2023

@author: Lenovo
"""

import numpy as np
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score

# 定义人名性别分类器类
class GenderClassifier:
    def __init__(self):
        # 定义感知机算法模型
        self.model = Perceptron(max_iter=100, tol=1e-2)

    # 定义训练函数
    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    # 定义预测函数
    def predict(self, X_test):
        return self.model.predict(X_test)
# 定义字典大小和人名最大长度
dict_size = 5000
max_len = 10
# 定义训练数据
names = ['张吉惟', '林国瑞', '林玟书', '江奕云', '林子帆', '夏志豪', '洪振霞',
         '菲利普','马歇尔','威廉','克拉伦斯','詹森','雷尔夫','弗雷德里克']
#
labels = [1,1,1,1,1,1,1,
          0,0,0,0,0,0,0]

# 构建字典
char_dict = {}
for name in names:
    for char in name:
        if char not in char_dict:
            char_dict[char] = len(char_dict)

# 定义编码函数
def encode_name(name):
    #如果字典中没有该字符则将该字符加入字典
    for char in name:
        if char not in char_dict:
            char_dict[char] = len(char_dict)
    # 将人名转换为定长向量
    name_vec = np.zeros(max_len, dtype=int)
    for i, char in enumerate(name):
        name_vec[i] = char_dict[char]
    return name_vec

# 对训练数据进行编码
X_train = np.array([encode_name(name) for name in names])
print(X_train)

y_train = np.array(labels)

# 定义测试数据
X_test = np.array([encode_name(name) for name in ['艾伦', '陈丽华', '刘华东','托马斯']])
y_test=[0,1,1,0]

# 对向量进行归一化
X_train = (X_train - np.min(X_train)) / (np.max(X_train) - np.min(X_train))
X_test = (X_test - np.min(X_test)) / (np.max(X_test) - np.min(X_test))
# 创建人名性别分类器对象
classifier = GenderClassifier()

# 训练模型
classifier.train(X_train, y_train)

# 预测性别
y_pred = classifier.predict(X_test)

# 计算准确率
accuracy = accuracy_score(y_test, y_pred)

# 输出结果
print("预测结果：", y_pred)
print("准确率：", accuracy)
