# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 11:04:44 2023

@author: Lenovo
"""

import cv2 as cv

v = cv.VideoCapture(0,cv.CAP_DSHOW)
# 打开狗头的图片
head = cv.imread('GouTou.png')
face_detector = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
while True:
    flag, frame = v.read()
    if flag == False:
        break
    faces = face_detector.detectMultiScale( frame )
    for x,y,w,h in faces:
        head2 = cv.resize( head, dsize=(w, h))
        # frame[y:y+h, x:x+w] = head2
        for i in range(1, head2.shape[0] ): #遍历狗头的高
            for j in range(1,  head2.shape[1] ): #狗头的宽
                if (head2[i,j] < 10).all() : #像素颜色是类似黑色的不用管
                    pass
                else:
                    frame[i+y,j+x] = head2[i,j]


    cv.imshow('img', frame)
    key = cv.waitKey(1000//30)
    if key == ord('q'):
        break