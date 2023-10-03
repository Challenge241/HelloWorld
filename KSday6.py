# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 09:02:19 2023

@author: Lenovo
"""

import cv2 as cv

# 读取图片
img = cv.imread('C:/Users/Lenovo/Desktop/R.png')
# 宽高
print( img.shape )  # (高度, 宽度, 颜色通道)
"""
BGR:  颜色通道顺序  b=蓝  g=绿 r=红
"""
#设置宽高
# cv.resize(img, dsize=(宽度， 高度 ) )
img2 = cv.resize(img, dsize=(320, 405) )

# 彩图更改为灰度
gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
print( gray.shape )
#查看
cv.imshow('img', img)
cv.imshow('img2', img2)
cv.imshow('gray', gray)
cv.waitKey(0) #持续化的执行  0 = 永久不关
cv.destroyAllWindows() # 关闭所有窗口，释放内存

import cv2 as cv

img = cv.imread('C:/Users/Lenovo/Desktop/R.png')
# hsv
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
"""   [ b, g, r ] 
色调（H）   0-180   b
饱和度（S）   g
亮度（V）   r
"""

cv.imshow('img', img)
cv.imshow('hsv', hsv)
cv.waitKey(0) #持续化的执行  0 = 永久不关
cv.destroyAllWindows() 

import cv2 as cv
import numpy as np


img = cv.imread('C:/Users/Lenovo/Desktop/R.png')

# 第一种方式
# img1 = cv.resize(img, dsize=( img.shape[1]//4, img.shape[0]//4  ) )
# res_img = cv.resize(img1, dsize=(img.shape[1], img.shape[0]) )
# cv.imshow('img', img)
# cv.imshow('img1', img1)
# cv.imshow('res_img', res_img)
# cv.waitKey(0) #持续化的执行  0 = 永久不关
# cv.destroyAllWindows() #

img1 = img[::10, ::10]
img2 = np.repeat(img1, 10, axis=1)
img3 = np.repeat(img2, 10, axis=0)


cv.imshow('img', img)
cv.imshow('img1', img1)
cv.imshow('img3', img3)
cv.waitKey(0) #持续化的执行  0 = 永久不关
cv.destroyAllWindows() 

import numpy as np


# res = np.array([1,2,3,4,5])
# data = np.repeat( res, 3 )
# print( data )

res = np.array(
    [
        [1,2,3],
        [4,5,6]
    ]
)
print( res )
data = np.repeat(res, 3, axis=1)
print( data )
data1 = np.repeat( data, 3, axis=0)
print( data1 )