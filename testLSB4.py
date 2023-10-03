# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 16:21:58 2023

@author: Lenovo
"""

from PIL import Image

def extract_watermark(image_path):
    # 打开图像并转换为 RGB 模式
    image = Image.open(image_path).convert('RGB')
    # 获得图像的宽度和高度
    width, height = image.size
    # 创建一个变量来存储提取的二进制数据
    extracted_bits = ''
    # 遍历图像的每个像素
    for y in range(height):
        for x in range(width):
            # 获得当前像素的 RGB 值
            r, g, b = image.getpixel((x, y))
            # 提取 r, g, b 的最低4位，并添加到二进制数据中
            extracted_bits += format(r & 0x0F, '04b')
            extracted_bits += format(g & 0x0F, '04b')
            extracted_bits += format(b & 0x0F, '04b')
    # 将二进制数据转换为文字
    watermark_text = ''
    for i in range(0, len(extracted_bits), 8):
        byte = extracted_bits[i:i+8]
        if byte == '00000000':
            break  # 遇到 null 字符时停止
        watermark_text += chr(int(byte, 2))
    return watermark_text

# 提取水印
print(extract_watermark(b'D:\TryShuiYin\GouTou.png'))
