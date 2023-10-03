# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 11:01:14 2023

@author: Lenovo
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM

# 数据预处理
df = pd.read_csv('AAPL.csv')  # AAPL 是苹果公司的股票代码，你可以替换为任何有效的股票代码
df = df['Close'].values
df = df.reshape(-1, 1)

# 数据归一化
scaler = MinMaxScaler(feature_range=(0, 1))
df = scaler.fit_transform(df)

# 数据集划分
train_size = int(len(df) * 0.8)
train_set, test_set = df[0:train_size], df[train_size:]

# 转换为适合 LSTM 输入的数据形状
def create_dataset(df):
    x, y = [], []
    for i in range(50, len(df)):
        x.append(df[i-50:i, 0])
        y.append(df[i, 0])
    x = np.array(x)
    y = np.array(y)
    return x, y

x_train, y_train = create_dataset(train_set)
x_test, y_test = create_dataset(test_set)

# 为 LSTM 准备适当的形状
x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

# 建立 LSTM 模型
model = Sequential()
model.add(LSTM(units=96, return_sequences=True, input_shape=(x_train.shape[1], 1)))
model.add(LSTM(units=96))
model.add(Dense(1))

# 训练模型
model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(x_train, y_train, epochs=50, batch_size=32)

# 预测
predictions = model.predict(x_test)
predictions = scaler.inverse_transform(predictions)

# 绘制结果
plt.figure(figsize=(10, 6))
plt.plot(df, color='blue', label='Actual Apple Stock Price')
plt.plot(range(len(y_train)+50, len(y_train)+50+len(predictions)), predictions, color='red', label='Predicted Apple Stock Price')
plt.title('Apple Stock Price Prediction')
plt.xlabel('Date')
plt.ylabel('Apple Stock Price')
plt.legend()
plt.show()
