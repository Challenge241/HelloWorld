# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 09:11:42 2023

@author: Lenovo
"""

import cv2

# 加载预训练的人脸检测模型
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 读取图像
img = cv2.imread('C:/Users/Lenovo/Desktop/R.png')

# 转为灰度图像
#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 进行人脸检测
faces = face_cascade.detectMultiScale(
    img,
    scaleFactor=1.18,
    minNeighbors=5,
    #maxSize=(75,75),
    minSize=(30,30)
    )

# 在每个检测到的人脸周围绘制矩形框
for (x, y, w, h) in faces:
    #在图像img上，以(x, y)为左上角，(x+w, y+h)为右下角，颜色为红色，线条厚度为2的位置画一个矩形。
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
'''
#将窗口显示在别的位置，因为有时候会出bug，不知道怎么回事，显示出来的窗口在最左侧    
# 创建一个窗口
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
# 获取屏幕的尺寸
screen_width = cv2.getWindowImageRect('image')[2]
screen_height = cv2.getWindowImageRect('image')[3]
# 计算窗口应该位于的位置
x = (screen_width - img.shape[1]) // 2
y = (screen_height - img.shape[0]) // 2
# 移动窗口
cv2.moveWindow('image', x, y)
'''
# 显示图像
cv2.imshow('image', img)

# 等待按键操作，然后关闭窗口
cv2.waitKey(0)
cv2.destroyAllWindows()
