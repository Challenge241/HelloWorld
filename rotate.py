# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 17:05:34 2023

@author: Lenovo
"""

from PIL import Image
# 打开图像
image = Image.open(r'D:\TryChangeTu\expanded_image.png')

# 旋转图像
angle = 45  # 旋转角度
resampled_image = image.rotate(angle, resample=Image.BICUBIC)

# 保存旋转后的图像
resampled_image.save(r'D:\TryChangeTu\rotateTKK.png')


