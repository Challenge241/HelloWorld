# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 15:50:37 2023

@author: Lenovo
"""
#不知道怎么回事，报错且始终解决不了，问chatGPT4也没用，原来chatGPT4的能力是有极限的
import cv2
import numpy as np
def extract_watermark(image_path, watermark_length):
    # 读取图像
    img = cv2.imread(image_path)
    # 转换为 YUV 色彩空间
    yuv_img = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
    # 取出 Y 通道（亮度）
    y, u, v = cv2.split(yuv_img)
    # 对 Y 通道应用离散余弦变换
    dct_y = cv2.dct(np.float32(y))
    # 提取水印
    flat_dct_y = dct_y.flatten()
    watermark = [0 if flat_dct_y[i] > 0 else 1 for i in range(watermark_length * 8)]
    # 解码水印
    watermark_bytes = [int(''.join(map(str, watermark[i:i+8])), 2) for i in range(0, len(watermark), 8)]
    watermark_text = ''.join(chr(b) for b in watermark_bytes)
    return watermark_text

watermark_text = extract_watermark(r'D:\TryShuiYin\DCTedImage.png', len('Hello, world!'))
print(watermark_text)
        