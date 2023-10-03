# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 16:19:03 2023

@author: Lenovo
"""

from PIL import Image
import cv2
def add_watermark(image_path, watermark_text, output_path):
    # 打开图像并转换为 RGB 模式
    image = Image.open(image_path).convert('RGB')
    # 获得图像的宽度和高度
    width, height = image.size
    # 转换水印文本为二进制数据
    watermark_bits = ''.join(format(ord(c), '08b') for c in watermark_text)
    watermark_bits += '00000000'  # 添加一个 null 字符表示文本的结束
    # 遍历图像的每个像素
    idx = 0
    for y in range(height):
        for x in range(width):
            # 获得当前像素的 RGB 值
            r, g, b = image.getpixel((x, y))
            # 如果还有水印数据没有编码
            if idx < len(watermark_bits):
                # 将水印数据编码到 r 的最低4位
                r = (r & 0xF0) | int(watermark_bits[idx:idx+4], 2)
                idx += 4
            if idx < len(watermark_bits):
                # 将水印数据编码到 g 的最低4位
                g = (g & 0xF0) | int(watermark_bits[idx:idx+4], 2)
                idx += 4
            if idx < len(watermark_bits):
                # 将水印数据编码到 b 的最低4位
                b = (b & 0xF0) | int(watermark_bits[idx:idx+4], 2)
                idx += 4
            # 设置像素的新 RGB 值
            image.putpixel((x, y), (r, g, b))
    # 保存图像
    image.save(output_path)

shuiyinText='6666666'

# 添加水印
add_watermark(b'D:\GouTouTu\img30_Skirt with Lacing_$34.99.png', shuiyinText, 'D:\TryShuiYin\GouTou.png')
#img = cv2.imread('D:\TryShuiYin\watermarked.png')
#cv2.imshow('Image Window', img)