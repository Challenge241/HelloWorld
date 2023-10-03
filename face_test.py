# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 11:45:01 2023

@author: Lenovo
"""

import cv2

# 加载预训练的人脸分类器
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 打开摄像头
cap = cv2.VideoCapture(0)

while True:
    # 读取一帧
    ret, frame = cap.read()
    
    # 将图像转为灰度图像，因为opencv人脸检测器需要灰度图像
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # 人脸检测
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    # 画出人脸框
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
    # 显示图像
    cv2.imshow('Video', frame)
    
    # 按q键退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 关闭摄像头
cap.release()
# 关闭窗口
cv2.destroyAllWindows()
