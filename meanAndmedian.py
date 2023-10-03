# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 10:57:12 2023

@author: Lenovo
"""

import pandas as pd

# 读取csv文件
df = pd.read_csv('books.csv')

# 计算平均值
mean_value = df["Price"].str.replace('Â£', '').astype(float).mean()
print(f'Mean: {mean_value}')

# 计算中位数
median_value = df["Price"].str.replace('Â£', '').astype(float).median()
print(f'Median: {median_value}')