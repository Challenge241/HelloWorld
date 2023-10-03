# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 20:18:18 2023

@author: Lenovo
"""
'''
我发现用LSB算法提取以.png为后缀的图片的水印没问题，提取以.jpg为后缀的图片会出现乱码
这个问题的原因可能在于JPEG的压缩方式。
当你将图像保存为JPEG格式时，它会使用一种名为离散余弦变换（DCT）的技术对图像进行压缩。
这种压缩是有损的，意味着它会丢失一些图像的信息。
特别地，它可能会更改图像的某些像素值，这就是为什么在对JPEG图像使用最低有效位（LSB）隐写术时可能会出现问题的原因。
另一方面，PNG是一种无损压缩格式，它不会更改图像的任何像素值。
因此，当你在PNG图像上使用LSB隐写术时，你可以完全恢复出原来的数据。
因此，如果你打算使用LSB隐写术，我建议你使用PNG或其他无损压缩格式，避免使用JPEG或其他可能更改像素值的有损压缩格式。
'''
from PIL import Image
import os
import glob

# 指定输入和输出文件夹
input_folder = 'D:\\GouTouTu\\'
output_folder = 'D:\\GouTouPng\\'

# 确保输出文件夹存在
os.makedirs(output_folder, exist_ok=True)

# 遍历文件夹中的所有.jpg文件
for jpg_file in glob.glob(input_folder + '*.jpg'):
    # 打开.jpg文件
    image = Image.open(jpg_file)
    # 生成.png的文件名
    png_file = os.path.splitext(os.path.basename(jpg_file))[0] + '.png'
    # 构造完整的输出路径
    output_path = os.path.join(output_folder, png_file)
    # 保存为.png文件
    image.save(output_path)

print("所有.jpg图片已转换为.png")
