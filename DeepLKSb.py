# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 10:40:52 2023

@author: Lenovo
"""

import os
import cv2
from PIL import Image

input_folder = 'D:\\PaQv4399TU'
output_folder = 'D:\\PQ4399TUgai'

# 确保输出文件夹存在，如果不存在则创建
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 遍历输入文件夹中的所有文件
for filename in os.listdir(input_folder):
    # 只处理jpg和png文件
    if filename.endswith('.jpg') or filename.endswith('.png'):
        input_filepath = os.path.join(input_folder, filename)
        # 使用PIL将图片转化为灰度图像
        img = Image.open(input_filepath).convert('L')
        # 保存灰度图像到输出文件夹
        output_filepath = os.path.join(output_folder, filename)
        img.save(output_filepath)
        # 使用OpenCV读取灰度图像
        img = cv2.imread(output_filepath, cv2.IMREAD_GRAYSCALE)
        # 使用中值滤波进行噪声过滤
        img = cv2.medianBlur(img, 5)
        # 保存处理后的图片到输出文件夹
        cv2.imwrite(output_filepath, img)
