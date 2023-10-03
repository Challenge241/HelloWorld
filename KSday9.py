# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 14:14:07 2023

@author: Lenovo
"""

# 导入OpenCV库
import cv2 as cv
# 导入os库，用于处理文件和目录
import os

# 创建一个视频捕获对象，参数0表示使用默认的摄像头
v = cv.VideoCapture(0)

# 导入Haar特征的人脸检测分类器
face_detector = cv.CascadeClassifier('haarcascade_frontalface_alt.xml')

# 初始化人名和文件名编号
name = ''
filename = 0

# 循环读取视频帧
while True:
    # 读取一帧视频，flag表示是否读取成功，frame是读取的帧
    flag, frame = v.read()

    # 如果读取失败，退出循环
    if flag == False:
        break

    # 将彩色帧转换为灰度帧
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # 使用人脸检测分类器检测灰度帧中的人脸
    faces = face_detector.detectMultiScale(gray)

    # 遍历所有检测到的人脸
    for x,y,w,h in faces:
        # 提取人脸区域
        face = gray[ y:y+h, x:x+w ]

        # 如果已经输入了人名，将人脸区域保存为图像
        if  name:
            cv.imwrite('face/{}/{}.jpg'.format(name, filename), face )
            filename += 1

        # 在原彩色帧上绘制人脸的矩形框
        cv.rectangle(
            frame,
            pt1=( x,y),
            pt2=(x+w, y+h),
            color=[0,255,0],
            thickness=2
        )
    # 如果保存的图像数量超过30，重置人名和文件名编号，并打印提示信息
    if filename > 30:
        name = ''
        filename = 0
        print('数据保存成功！')

    # 显示带有人脸矩形框的彩色帧
    cv.imshow('img', frame)

    # 等待30ms，并获取按下的键的ASCII码
    key = cv.waitKey(1000//30)

    # 如果按下的键是'w'，则要求用户输入保存的人名，如果对应的目录不存在，则创建该目录
    if key == ord('w'):
        name = input('请输入保存的人名（拼音）:')
        if os.path.exists('face/'+ name ):
            pass
        else:
            os.mkdir( 'face/'+ name)

    # 如果按下的键是'q'，则退出循环
    if key == ord('q'):
        break
