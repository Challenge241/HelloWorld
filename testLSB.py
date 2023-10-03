# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 11:04:18 2023

@author: Lenovo
"""

from PIL import Image

def extract_watermark(image_path):
    # 打开图像并转换为 RGB 模式
    image = Image.open(image_path).convert('RGB')
    # 获得图像的宽度和高度
    width, height = image.size
    # 用来存储提取出的水印位
    watermark_bits = ''
    # 遍历图像的每个像素
    for y in range(height):
        for x in range(width):
            # 获得当前像素的 RGB 值
            r, g, b = image.getpixel((x, y))
            # 提取 r 的最低有效位
            watermark_bits += str(r & 0x01)
            # 提取 g 的最低有效位
            watermark_bits += str(g & 0x01)
            # 提取 b 的最低有效位
            watermark_bits += str(b & 0x01)
    # 将提取出的水印位转换为文本
    watermark_text = ''.join(chr(int(watermark_bits[i:i+8], 2)) for i in range(0, len(watermark_bits), 8))
    # 返回提取出的水印文本，直到遇到 null 字符为止
    return watermark_text.split('\x00', 1)[0]

# 提取水印
watermark_text = extract_watermark('D:\TryShuiYin\watermarked.png')
print('Watermark Text:', watermark_text)
