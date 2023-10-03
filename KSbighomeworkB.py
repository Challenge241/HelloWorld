# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 17:51:57 2023

@author: Lenovo
"""

import cv2 as cv
import os
import glob

# 打开狗头的图片
head = cv.imread('GouTou.png')
# 加载OpenCV的人脸检测器
face_detector = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
# 遍历文件夹中的所有图片
for filename in glob.glob("D:\\scarpingClubPic\\*.jpg"):
    # 读取图片
    img = cv.imread(filename)
    # 进行人脸检测
    faces = face_detector.detectMultiScale(
        img,
        scaleFactor=1.18,
        minNeighbors=5,
        #maxSize在这里好像作用不大
        minSize=(30,30)
        )
    # 如果检测到了人脸
    if len(faces) > 0:
        # 只取可能性最大的人脸
        x, y, w, h = faces[0]
        '''
        这样的排序是基于detectMultiScale函数的工作原理。
        这个函数使用滑动窗口和图像金字塔的方式在不同的位置和尺度下检测人脸，
        然后计算每个窗口中的特征与预训练模型中的人脸特征的匹配程度，最后返回匹配程度最高的窗口。
        所以，faces[0]就是可能性最大的人脸，faces[1]是可能性第二大的人脸，
        以此类推。如果你只想处理可能性最大的人脸，那么只需要使用faces[0]就可以了。
        '''
        # 调整狗头的大小以匹配人脸
        head2 = cv.resize(head, (w, h))
        # 将狗头覆盖在人脸上
        for i in range(head2.shape[0]):
            for j in range(head2.shape[1]):
                if (head2[i, j] < 10).all():  # 如果像素颜色接近黑色，则跳过
                    continue
                else:
                    img[y+i, x+j] = head2[i, j]
        # 保存添加了狗头的图片
        new_filename = "D:\\GouTouTu\\" + os.path.basename(filename)
        cv.imwrite(new_filename, img)
print("完成了所有图片的狗头添加。")
