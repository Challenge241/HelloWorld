# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 10:51:34 2023

@author: Lenovo
"""
#隐形水印
from PIL import Image
#transparency透明度
def add_watermark(image_path, watermark_path, output_path, transparency):
    # 打开原图和水印图片
    image = Image.open(image_path)
    watermark = Image.open(watermark_path)
    # 确保水印图片的大小和原图一样
    watermark = watermark.resize(image.size)
    # 创建一个新的图片来存放结果
    result = Image.new('RGBA', image.size)
    # 将原图和水印图片合并到结果图片
    for x in range(image.width):
        for y in range(image.height):
            image_pixel = image.getpixel((x, y))
            watermark_pixel = watermark.getpixel((x, y))
            # 使用透明度计算结果像素
            new_pixel = tuple(
                int(image_pixel[i] * (1 - transparency) + watermark_pixel[i] * transparency)
                for i in range(3)
            ) + (255,)
            result.putpixel((x, y), new_pixel)
    # 保存结果图片
    result.save(output_path)
originalpath='D:\TryShuiYin\TKK.png'
watermarkpath='D:\TryShuiYin\star_watermark.png'
outputpath='D:\TryShuiYin\YXSY.png'
# 添加水印
add_watermark(originalpath, watermarkpath, outputpath, 0.2)
