# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 00:09:21 2023

@author: Lenovo
"""

import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.widgets import Button

# 获取D:\PaQv文件夹下所有图片
image_directory = 'D:\\PaQv'
image_files = [os.path.join(image_directory, file) for file in os.listdir(image_directory) if file.endswith(('.png', '.jpg', '.jpeg'))]
current_image = 0

# 创建一个画布
fig, ax = plt.subplots()

# 显示初始图片
image = mpimg.imread(image_files[current_image])
imgplot = plt.imshow(image)

# 定义翻页函数
def next_image(event):
    global current_image
    current_image = (current_image + 1) % len(image_files)
    image = mpimg.imread(image_files[current_image])
    imgplot.set_data(image)
    plt.draw()

def prev_image(event):
    global current_image
    current_image = (current_image - 1) % len(image_files)
    image = mpimg.imread(image_files[current_image])
    imgplot.set_data(image)
    plt.draw()

# 创建前一个和后一个按钮
axprev = plt.axes([0.7, 0.05, 0.1, 0.075])
axnext = plt.axes([0.81, 0.05, 0.1, 0.075])
bnext = Button(axnext, 'Next')
bnext.on_clicked(next_image)
bprev = Button(axprev, 'Previous')
bprev.on_clicked(prev_image)

plt.show()
