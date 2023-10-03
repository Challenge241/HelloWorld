# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 10:34:00 2023

@author: Lenovo
"""

import cv2
import face_recognition

# 加载你的图片并学习如何识别它们
einstein_image = face_recognition.load_image_file(r"C:\Users\Lenovo\Desktop\Einstein1921.jpg")
einstein_face_encoding = face_recognition.face_encodings(einstein_image)[0]


maxwell_image = face_recognition.load_image_file(r"C:\Users\Lenovo\Desktop\maxwell.jpg")
maxwell_face_encoding = face_recognition.face_encodings(maxwell_image)[0]

# 创建一个数组，其中包含已知面部编码及其名称
known_face_encodings = [
    einstein_face_encoding,
    maxwell_face_encoding
]
known_face_names = [
    "Barack Obama",
    "Joe Biden"
]

# 加载我们要识别的图片
unknown_image = face_recognition.load_image_file(r"C:\Users\Lenovo\Desktop\AlbertEinstein.jpg")

# 寻找图像中的所有人脸及面部编码
face_locations = face_recognition.face_locations(unknown_image)
face_encodings = face_recognition.face_encodings(unknown_image, face_locations)

# 将未知的脸与我们已知的脸进行比较
for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    # 判断是否与已知面部匹配
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

    name = "Unknown"

    if True in matches:
        first_match_index = matches.index(True)
        name = known_face_names[first_match_index]

    # 在图片上画出人脸，并标注名字
    cv2.rectangle(unknown_image, (left, top), (right, bottom), (0, 0, 255), 2)
    cv2.rectangle(unknown_image, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
    cv2.putText(unknown_image, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 255, 255), 1)

# 展示结果图片
cv2.imshow('Image', unknown_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
