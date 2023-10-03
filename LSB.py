# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 11:03:45 2023

@author: Lenovo
"""
#后4位有效位技术加水印
from PIL import Image

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
                # 将水印数据编码到 r 的最低有效位
                r = (r & 0xFE) | int(watermark_bits[idx])
                idx += 1
            if idx < len(watermark_bits):
                # 将水印数据编码到 g 的最低有效位
                g = (g & 0xFE) | int(watermark_bits[idx])
                idx += 1
            if idx < len(watermark_bits):
                # 将水印数据编码到 b 的最低有效位
                b = (b & 0xFE) | int(watermark_bits[idx])
                idx += 1
            # 设置像素的新 RGB 值
            image.putpixel((x, y), (r, g, b))
    # 保存图像
    image.save(output_path)
shuiyinText='6666666'
# 添加水印
add_watermark('D:\TryShuiYin\TKK.png', shuiyinText, 'D:\TryShuiYin\watermarked.png')
