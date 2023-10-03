# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 10:05:06 2023

@author: Lenovo
"""

import easyocr

# 创建一个 reader 对象，指定使用的语言
reader = easyocr.Reader(['en'])

# 从图像中读取文本
result = reader.readtext(b'C:\Users\Lenovo\Desktop\TryOCR.png')  # 将 'image.jpg' 替换为你要处理的图像的路径

# 打印结果
for detection in result:
    # detection 包含文本区域的坐标和识别的文本
    top_left = tuple(detection[0][0])
    bottom_right = tuple(detection[0][2])
    text = detection[1]
    print(f'Text: {text}, Coordinates: {top_left}, {bottom_right}')
