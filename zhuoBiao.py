# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 09:57:09 2023

@author: Lenovo
"""
'''
import cv2

# 鼠标回调函数
def get_coordinates(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONUP:
        print('x = %d, y = %d' %(x, y))

# 读取图像
img = cv2.imread('C:/Users/Lenovo/Desktop/BBS.png')

# 创建一个名为 'image' 的窗口，并将鼠标回调函数绑定到这个窗口
cv2.namedWindow('image')
cv2.setMouseCallback('image', get_coordinates)

# 显示图像，等待鼠标点击
while True:
    cv2.imshow('image', img)
    if cv2.waitKey(20) & 0xFF == 27:  # 按下 'esc' 键退出
        break

cv2.destroyAllWindows()
'''
'''
import cv2
import time
# 鼠标回调函数
def get_coordinates(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONUP:
        print('x = %d, y = %d' %(x, y))

# 读取图像
img = cv2.imread('C:/Users/Lenovo/Desktop/BBS.png')

# 创建一个名为 'image' 的窗口，并将鼠标回调函数绑定到这个窗口
cv2.namedWindow('image')
cv2.setMouseCallback('image', get_coordinates)
cv2.imshow('image', img)
# 显示图像，等待鼠标点击
while True:
    if cv2.getWindowProperty('image', cv2.WND_PROP_VISIBLE) < 1:  # 窗口被关闭时退出
        break
    if cv2.waitKey(20) & 0xFF == 27:  # 按下 'esc' 键退出
        break

cv2.destroyAllWindows()
'''
'''
import cv2

# 鼠标回调函数
def get_coordinates(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONUP:
        print('x = %d, y = %d' %(x, y))

# 读取图像
img = cv2.imread('C:/Users/Lenovo/Desktop/BBS.png')

# 创建一个名为 'image' 的窗口，并将鼠标回调函数绑定到这个窗口
cv2.namedWindow('image')
cv2.setMouseCallback('image', get_coordinates)
cv2.imshow('image', img)
# 显示图像，等待鼠标点击
while True:
    if cv2.waitKey(1) != -1:  # 用户按下了一个键或者关闭了窗口
        break

cv2.destroyAllWindows()
'''
'''
import cv2

# 鼠标回调函数
def get_coordinates(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONUP:
        print('x = %d, y = %d' %(x, y))

# 读取图像
img = cv2.imread('C:/Users/Lenovo/Desktop/BBS.png')

# 创建一个名为 'image' 的窗口，并将鼠标回调函数绑定到这个窗口
cv2.namedWindow('image')
cv2.setMouseCallback('image', get_coordinates)

# 显示图像，等待鼠标点击
while True:
    # 窗口不存在，跳出循环
    if cv2.getWindowProperty('image', 0) == -1:  
        break

    cv2.imshow('image', img)

    if cv2.waitKey(1) & 0xFF == 27:  # 按下 'esc' 键退出
        break

cv2.destroyAllWindows()
'''
import cv2

# 鼠标回调函数
def get_coordinates(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONUP:
        print('x = %d, y = %d' %(x, y))

# 读取图像
img = cv2.imread('C:/Users/Lenovo/Desktop/BBS.png')

# 创建一个名为 'image' 的窗口，并将鼠标回调函数绑定到这个窗口
cv2.namedWindow('image')
cv2.setMouseCallback('image', get_coordinates)

# 显示图像，等待鼠标点击
while True:
    try:
        # 检查窗口是否存在
        if cv2.getWindowProperty('image', 0) == -1:  
            break
    except:
        break  # 如果尝试获取窗口属性时发生错误，我们同样退出循环

    cv2.imshow('image', img)

    if cv2.waitKey(1) & 0xFF == 27:  # 按下 'esc' 键退出
        break

cv2.destroyAllWindows()
