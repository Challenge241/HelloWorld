# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 09:09:01 2023

@author: Lenovo
"""

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
import numpy as np

# 创建模拟数据集
X, y = make_classification(n_samples=1000, n_features=20, n_informative=15, n_redundant=5, random_state=6)
# 转换y的标签到1和-1
y = np.where(y==0, -1, 1)
# 分割数据集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 定义弱分类器个数
n_clf = 10

# 初始化权重
w = np.full(X_train.shape[0], 1/X_train.shape[0])

# 存储所有的弱分类器
clfs = []

for _ in range(n_clf):
    # 训练一个弱分类器
    clf = DecisionTreeClassifier(max_depth=1, max_leaf_nodes=2)
    clf.fit(X_train, y_train, sample_weight=w)
    # 计算预测值和错误率
    predictions = clf.predict(X_train)
    error = w[(predictions != y_train)].sum()
    # 计算分类器权重
    clf_weight = 0.5 * np.log((1 - error) / error)
    # 更新数据权重
    w = w * np.exp(-clf_weight * y_train * predictions)
    w = w / w.sum()
    # 保存分类器
    clfs.append((clf, clf_weight))

# 使用训练的模型进行预测
y_test_pred = 0
for clf, clf_weight in clfs:
    y_test_pred += clf_weight * clf.predict(X_test)

y_test_pred = np.sign(y_test_pred)

print(f'Accuracy: {accuracy_score(y_test, y_test_pred)}')
