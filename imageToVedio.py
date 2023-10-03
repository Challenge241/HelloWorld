# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 09:45:56 2023

@author: Lenovo
"""

import cv2
import os

# 图片所在目录
image_folder = 'images'
# 视频名称
video_name = 'video.avi'

# 获取图片列表
images = [img for img in os.listdir(image_folder) if img.endswith(".png") or img.endswith(".jpg")]
# 按文件名排序
images.sort()

# 获取一张图片来确定帧的高度和宽度
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

# 视频编码，输出视频的帧率和帧大小
video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'XVID'), 30, (width,height))

# 将图片添加到视频中
for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

# 释放视频
video.release()
