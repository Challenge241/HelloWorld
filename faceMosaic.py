# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 10:50:13 2023

@author: Lenovo
"""
'''
import cv2
import numpy as np

def mosaic(img, rect, size):
    # 获取矩形区域
    (x1, y1, x2, y2) = rect
    w = x2 - x1
    h = y2 - y1
    # 将矩形区域的图像缩小然后再放大，实现马赛克效果
    iRect = img[y1:y2, x1:x2]
    iSmall = cv2.resize(iRect, (size, size))
    iMosaic = cv2.resize(iSmall, (w, h))
    # 将马赛克效果的图像放回原图
    img[y1:y2, x1:x2] = iMosaic
    return img

# 加载人脸分类器
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 读取图像
img = cv2.imread('C:/Users/Lenovo/Desktop/R.png')

# 转换为灰度图像
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 检测人脸
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

# 对每个检测到的人脸进行马赛克处理
for (x, y, w, h) in faces:
    img = mosaic(img, (x, y, x+w, y+h), 10)

# 显示图像
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
import cv2
import numpy as np

# 加载人脸识别分类器
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 定义马赛克函数
def mosaic_area(img, x, y, w, h, size=10):
    # 截取目标区域
    face_img = img[y:y+h, x:x+w]
    # 缩小
    small = cv2.resize(face_img, (size, size))
    # 放大
    mosaic = cv2.resize(small, (w, h), interpolation=cv2.INTER_NEAREST)
    # 替换原图像
    img[y:y+h, x:x+w] = mosaic
    return img

# 读取图像
img = cv2.imread('C:/Users/Lenovo/Desktop/R.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 人脸识别
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

# 对检测到的每个人脸应用马赛克
for (x, y, w, h) in faces:
    img = mosaic_area(img, x, y, w, h)

# 显示图像
cv2.imshow('Mosaic', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

