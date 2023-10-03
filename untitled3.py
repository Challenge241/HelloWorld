# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 11:58:43 2023

@author: Lenovo
"""

# 导入需要的库
import matplotlib.pyplot as plt
import numpy as np
import cv2

# 读取并调整图像大小
img=cv2.imread('bathroom.jpg')
img_resize=cv2.resize(img,(768,480))

# 对图像进行高斯模糊处理
gaus=cv2.GaussianBlur(img_resize,(5,5),0)

# 将图像转换为灰度图像
gray = cv2.cvtColor(gaus, cv2.COLOR_BGR2GRAY)

# 使用Canny算子进行边缘检测
canny=cv2.Canny(gray,100,200)

# 获取图像的高度和宽度
height, width = canny.shape

# 计算图像的对角线长度
diag_len = int(np.ceil(np.sqrt(height ** 2 + width ** 2)))

# 初始化霍夫变换的累加器
accumulator = np.zeros((2 * diag_len, 180), dtype=np.uint8)

# 获取边缘图像中所有非零像素点的坐标
coords = np.argwhere(canny > 0)

# 对每一个坐标进行遍历，计算对应的霍夫变换参数
for x, y in coords:
    for t in range(-90, 90):
        r = int((x * np.cos(np.deg2rad(t))) + (y * np.sin(np.deg2rad(t))))
        accumulator[r + diag_len, t + 90] += 1

# 初始化直线集合
lines = []

# 获取霍夫变换的累加器中值大于等于150的坐标
for r, theta in np.argwhere(accumulator >= 150):
    lines.append((r - diag_len, theta - 90))

# 对每条直线进行遍历，绘制到原始图像中
for r, theta in lines:
    a = np.cos(np.deg2rad(theta))
    b = np.sin(np.deg2rad(theta))
    x0 = a * r
    y0 = b * r
    x1 = int(x0 + diag_len * (-b))
    y1 = int(y0 + diag_len * (a))
    x2 = int(x0 - diag_len * (-b))
    y2 = int(y0 - diag_len * (a))
    cv2.line(img_resize, (x1, y1), (x2, y2), (0, 0, 255), 2)

# 显示绘制好直线的图像
cv2.imshow('Hough',img_resize)

# 等待用户按下任意按键后，关闭所有图像窗口
cv2.waitKey(0)
cv2.destroyAllWindows()
