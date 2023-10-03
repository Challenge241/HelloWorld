# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 15:42:14 2023

@author: Lenovo
"""
#DCT
'''
使用OpenCV的Python库在图像的离散余弦变换（DCT）域添加水印。
但请注意，这个例子中的水印方法并不算特别强健，对图像的较大修改可能会破坏水印。
要实现真正强健的水印，可能需要更复杂的编码策略，或者使用机器学习等方法。
'''
import cv2
import numpy as np

def add_watermark(image_path, watermark_text, output_path):
    # 读取图像
    img = cv2.imread(image_path)
    # 转换为 YUV 色彩空间
    yuv_img = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
    # 取出 Y 通道（亮度）
    y, u, v = cv2.split(yuv_img)
    # 对 Y 通道应用离散余弦变换
    dct_y = cv2.dct(np.float32(y))
    # 创建水印
    watermark = [int(b) for b in ''.join(format(ord(c), '08b') for c in watermark_text)]
    # 添加水印到 DCT 系数中
    flat_dct_y = dct_y.flatten()
    for i, bit in enumerate(watermark):
        if (flat_dct_y[i] > 0 and bit == 0) or (flat_dct_y[i] < 0 and bit == 1):
            flat_dct_y[i] *= -1
    dct_y = flat_dct_y.reshape(dct_y.shape)
    # 应用逆 DCT
    y = cv2.idct(dct_y).astype(np.uint8)
    # 重新组合图像
    yuv_img = cv2.merge([y, u, v])
    watermarked_img = cv2.cvtColor(yuv_img, cv2.COLOR_YUV2BGR)
    # 保存图像
    cv2.imwrite(output_path, watermarked_img)


originalpath=r'D:\TryShuiYin\TKK.png'
shuiyinText=r'6'
outputpath=r'D:\TryShuiYin\DCTedImage.png'
# 添加水印
add_watermark(originalpath, shuiyinText, outputpath)