# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 17:11:51 2023

@author: Lenovo
"""

import cv2
#调整图像的尺寸
# 读取图像
image = cv2.imread(r'D:\TryChangeTu\TKK.png')

# 调整图像大小为新的宽度和高度
new_width = 800
new_height = 600
resized_image = cv2.resize(image, (new_width, new_height))

# 保存调整大小后的图像
cv2.imwrite(r'D:\TryChangeTu\resizedImage.png', resized_image)


#扩充
import cv2
import numpy as np

# 读取图像
image = cv2.imread(r'D:\TryChangeTu\TKK.png')

# 设置扩充的宽度和高度
new_width = image.shape[1] + 200
new_height = image.shape[0] + 200

# 创建一个黑色背景的图像
expanded_image = np.zeros((new_height, new_width, 3), dtype=np.uint8)

# 将原始图像放置在扩充图像中心
x = (new_width - image.shape[1]) // 2
y = (new_height - image.shape[0]) // 2
expanded_image[y:y+image.shape[0], x:x+image.shape[1]] = image

cv2.imwrite(r'D:\TryChangeTu\expanded_image.png',expanded_image)

'''
# 显示扩充后的图像
cv2.imshow('Expanded Image', expanded_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
'''
import cv2
import numpy as np

# 读取图像
image = cv2.imread(r'D:\TryChangeTu\TKK.png')

# 设置扩充的宽度和高度
new_width = image.shape[1] + 100
new_height = image.shape[0] + 100

# 创建一个白色背景的图像
expanded_image = np.ones((new_height, new_width, 3), dtype=np.uint8) * 255

# 将原始图像放置在扩充图像中心
x = (new_width - image.shape[1]) // 2
y = (new_height - image.shape[0]) // 2
expanded_image[y:y+image.shape[0], x:x+image.shape[1]] = image
cv2.imwrite(r'D:\TryChangeTu\expanded_image.png',expanded_image)
'''