# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 10:53:40 2023

@author: Lenovo
"""

'''
在这段代码中，我们用加水印后的像素值减去原图的像素值，然后再除以透明度，
来恢复出水印的像素值。但需要注意的是，这个方法只在理想情况下有效，
即只有在你知道原图、知道透明度，并且水印是通过简单的线性混合添加的情况下才有效。
而且，由于浮点数舍入误差和颜色空间可能的非线性，这个方法可能不会完全恢复出原来的水印图像。
在不知道原图的情况下，提取水印就需要用到更复杂的方法，比如频域分析，
但这已经超出了一般编程的范畴，需要图像处理和数字信号处理的专门知识。
'''
from PIL import Image
def extract_watermark(original_image_path, watermarked_image_path, output_path, transparency):
    # 打开原图和加水印后的图片
    original_image = Image.open(original_image_path)
    watermarked_image = Image.open(watermarked_image_path)
    # 创建一个新的图片来存放结果
    result = Image.new('RGBA', original_image.size)
    # 计算水印
    for x in range(original_image.width):
        for y in range(original_image.height):
            original_pixel = original_image.getpixel((x, y))
            watermarked_pixel = watermarked_image.getpixel((x, y))
            # 使用透明度和原图像素值来计算水印像素
            new_pixel = tuple(
                int((watermarked_pixel[i] - original_pixel[i] * (1 - transparency)) / transparency)
                for i in range(3)
            ) + (255,)
            result.putpixel((x, y), new_pixel)
    # 保存结果图片
    result.save(output_path)
originalpath=r'D:\TryShuiYin\TKK.png'
watermarkedImagepath=r'D:\TryShuiYin\YXSY.png'
outputpath=r'D:\TryShuiYin\testWatermark.png'
# 添加水印
extract_watermark(originalpath, watermarkedImagepath, outputpath, 0.1)
'''
在透明度与水印透明度不同时，能检测出水印的形状，不能检测出水印的真实颜色
'''