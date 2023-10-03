# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 09:45:44 2023

@author: Lenovo
"""

import cv2

# 读取图像
img = cv2.imread('C:/Users/Lenovo/Desktop/BBS4.png')

# 在图像上画一个矩形。参数依次是：图像、左上角坐标、右下角坐标、颜色、线宽
cv2.rectangle(img, (50, 50), (200, 200), (255, 0, 0), 2)

# 显示图像
cv2.imshow('Image', img)

# 等待按键操作，然后关闭窗口
cv2.waitKey(0)
cv2.destroyAllWindows()
