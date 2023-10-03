# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 17:21:28 2023

@author: Lenovo
"""

import cv2 as cv
import os
import glob

# 加载OpenCV的人脸检测器
face_detector = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 马赛克的大小，值越大，马赛克块越大
mosaic_size = 10

# 遍历文件夹中的所有图片
for filename in glob.glob("D:\\scarpingClubPic\\*.jpg"):
    # 读取图片
    img = cv.imread(filename)

    # 进行人脸检测
    faces = face_detector.detectMultiScale(img, scaleFactor=1.18, minNeighbors=5, minSize=(30,30))

    # 如果检测到了人脸
    if len(faces) > 0:
        # 只取可能性最大的人脸
        x, y, w, h = faces[0]

        # 对人脸区域进行马赛克处理
        face_area = img[y:y+h, x:x+w]
        face_area = cv.resize(face_area, (mosaic_size, mosaic_size))
        face_area = cv.resize(face_area, (w, h), interpolation=cv.INTER_NEAREST)
        img[y:y+h, x:x+w] = face_area

        # 保存添加了马赛克的图片
        new_filename = "D:\\MassicPic\\" + os.path.basename(filename)
        cv.imwrite(new_filename, img)

print("完成了所有图片的马赛克处理。")
