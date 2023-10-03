# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 10:51:12 2023

@author: Lenovo
"""

import cv2

# 加载人脸识别分类器
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 提取视频
cap = cv2.VideoCapture('C:/Users/Lenovo/Desktop/face.mp4')  # 如果你想要打开一个视频文件，你可以把0替换为视频文件的路径
#打开摄像头并获得摄像头的实时视频
#cap = cv2.VideoCapture(0)
while True:
    # 捕获一帧图像
    ret, frame = cap.read()
    if not ret:
        break

    # 转为灰度图
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 进行人脸识别
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # 在每个识别到的人脸周围画矩形
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # 显示结果
    cv2.imshow('Video', frame)

    # 按ESC退出
    if cv2.waitKey(1) & 0xFF == 27:  # 按下 'esc' 键退出
        break
    
cap.release()
cv2.destroyAllWindows()
