# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 17:02:22 2023

@author: Lenovo
"""

import numpy as np
from PIL import Image

# 打开图片
image = Image.open('D:\\TryChangeTu\\TKK.png')

# 转换为NumPy数组
image_array = np.array(image)

# 图像切片
cropped_image = image_array[100:300, 200:400, :]  # 切片从第100行到第300行，第200列到第400列，并保留所有通道

# 图像缩放
scaled_image = image.resize((500, 500))  # 缩放图像为500x500

# 图像旋转
rotated_image = image.rotate(45)  # 顺时针旋转图像45度

# 图像翻转
flipped_image = np.fliplr(image_array)  # 水平翻转图像

# 图像亮度调整
brightened_image = image.point(lambda x: x * 1.5)  # 增加图像亮度1.5倍

# 保存变换后的图片
cropped_image = Image.fromarray(cropped_image)
cropped_image.save('D:\\TryChangeTu\\cropped_image.png')

scaled_image.save('D:\\TryChangeTu\\scaled_image.png')

rotated_image.save('D:\\TryChangeTu\\rotated_image.png')

flipped_image = Image.fromarray(flipped_image)
flipped_image.save('D:\\TryChangeTu\\flipped_image.png')

brightened_image.save('D:\\TryChangeTu\\brightened_image.png')
