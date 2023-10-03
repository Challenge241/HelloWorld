# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 10:40:06 2023

@author: Lenovo
"""

'''
import cv2 as cv

img = cv.imread('./zhoujielun.jpg')

#  左上角 892,267  。   右下角 1105，531
#  ( x, y )
#画矩形
cv.rectangle(
    img,
    pt1=(887,267),  # 左上角坐标
    pt2=(1120,531), #右下角坐标
    color=[0, 0, 255],  #bgr
    thickness=2
)


cv.imshow('img', img)
cv.waitKey(0)

'''

'''
import cv2 as cv
import numpy as np


img = cv.imread('./zuifan.jpg')
#  310,125        386,211   x,y
# 310:386  x轴宽度
# 125:211  y轴高度
# 左上角 892,267  。   右下角 1105，531
# 267:531  892:1105
# 在原图进行提取人脸
face = img[125:211, 310:386   ]  #高度，宽度
face1 = face[::5, ::5]
#  80   16  整数
#  84     17 x 5  85
face2 = np.repeat(face1, 5, axis=1)
face3 = np.repeat(face2, 5, axis=0)
img[125:211, 310:386   ] = face3[:86, :76 ]

cv.imshow('face', face3)
cv.imshow('img', img)
cv.waitKey(0)
'''

'''
import cv2 as cv


img = cv.imread('sew.jpg')
# 使用级联分类器
face_detectro = cv.CascadeClassifier('haarcascade_frontalface_alt.xml')
# 用分类器进行检测人脸
faces = face_detectro.detectMultiScale(
    img,
    scaleFactor=1.18,  #缩放比例
    minNeighbors=5,   #相邻
    #  50 x 50
    # 其他的物体  60x 60
    maxSize=59,
    minSize=40
)
# faces保存多张人脸的坐标
for x,y,w,h in faces:
    print( x, y , w, h )
    # 左上角  x，y   右下角  x+w, y+h
    cv.rectangle(
        img,
        pt1=(x, y ), # 左上角
        pt2=( x+w, y+h), #右下角
        color=[255, 0, 0],  # bgr
        thickness=2
    )

cv.imshow('img', img)
cv.waitKey(0)

'''
import cv2 as cv

# 使用cv2.VideoCapture打开一个视频文件
v = cv.VideoCapture('C:/Users/Lenovo/Desktop/panda.mp4')

# 获取视频的帧率
fps = v.get(propId=cv.CAP_PROP_FPS)

# 获取视频的宽度和高度
ww = v.get(propId=cv.CAP_PROP_FRAME_WIDTH)
hh = v.get(propId=cv.CAP_PROP_FRAME_HEIGHT)

# 加载人脸识别分类器
face_detectroy = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    # 读取一帧
    flag , frame = v.read()

    # 如果读取失败（视频结束），则退出循环
    if flag == False:
        break

    # 缩小图像的尺寸
    frame1 = cv.resize(frame, dsize=( int(ww//2), int(hh//2))  )

    # 转为灰度图像
    gray = cv.cvtColor(frame1, cv.COLOR_BGR2GRAY)

    # 识别人脸
    faces = face_detectroy.detectMultiScale(gray)

    # 在每个识别到的人脸周围画矩形
    for x,y,w,h in faces:
        cv.rectangle(
            frame1,
            pt1=( x, y),
            pt2=(x+w, y+h),
            color=[207, 0, 193], # 粉色
            thickness=2
        )
    # 显示图像
    cv.imshow('img', frame1)

    # 等待键盘输入，参数为等待时间（毫秒）
    key = cv.waitKey(1000//30)

    # 如果按下 'q' 或 'Q' 键，退出循环
    if key == ord('q') or key == ord('Q'):
        break

    # 按下 'esc' 键退出
    if key & 0xFF == 27:
        break
