# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 09:11:16 2023

@author: Lenovo
"""
'''
import cv2  # 导入opencv库

# 读取图像
img = cv2.imread('image1.jpg')  # 将 'input.jpg' 替换为你要处理的图像的路径
print(img.shape)
#3个颜色通道的顺序为BGR蓝绿红
#设置宽高
#cv2.resize(img,dsize=(宽,高))
img=cv2.resize(img,dsize=(320,405))
print(img.shape)

# 将图像转化为灰度图像
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 显示原图和灰度图像
cv2.imshow('Original image', img)
cv2.imshow('Grayscale image', gray_img)

# 等待关闭窗口
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

'''
import cv2

# 加载图像并转化为灰度图像
img = cv2.imread('image1.jpg', cv2.IMREAD_GRAYSCALE)

# 应用直方图均衡化
equalized_img = cv2.equalizeHist(img)

# 显示原图和处理后的图像
cv2.imshow('Original image', img)
cv2.imshow('Equalized image', equalized_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
'''
'''
import cv2
import numpy as np

# 加载图像
img = cv2.imread('image1.jpg', cv2.IMREAD_GRAYSCALE)  # 将 'input.jpg' 替换为你要处理的图像的路径

# 归一化图像
normalized_img = np.zeros((800, 800))
normalized_img = cv2.normalize(img,  normalized_img, 0, 255, cv2.NORM_MINMAX)

# 显示原图和归一化后的图像
cv2.imshow('Original image', img)
cv2.imshow('Normalized image', normalized_img)

# 等待关闭窗口
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
'''
import cv2

# 加载原始的 RGB 图像
img = cv2.imread('image1.jpg')  # 将 'input.jpg' 替换为你要处理的图像的路径

# 将 RGB 图像转化为 HSV 图像,数值不变，数值含义变了，[b,g,r]依次变为了[h,s,v],例如r=30，则v=30
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# 显示原图和转化后的图像
cv2.imshow('Original image', img)
cv2.imshow('HSV image', hsv_img)

# 等待关闭窗口
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

'''
import cv2
import numpy as np

# 加载图像
img = cv2.imread('image1.jpg')

# 定义图像中需要进行校正的三个点以及他们在输出图像中对应的位置
pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

# 计算仿射变换矩阵
M = cv2.getAffineTransform(pts1, pts2)

# 使用仿射变换矩阵对图像进行变换
dst = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))

# 显示原始图像和校正后的图像
cv2.imshow('Input', img)
cv2.imshow('Output', dst)

# 等待用户关闭窗口
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
'''
import cv2

# 读取图像
img = cv2.imread('image1.jpg')  # 将 'input.jpg' 替换为你要处理的图像的路径

# 马赛克的大小，值越大，马赛克块越大
mosaic_size = 15

# 将图像缩小，然后再放大，达到马赛克的效果
small = cv2.resize(img, (img.shape[1] // mosaic_size, img.shape[0] // mosaic_size))
mosaic_img = cv2.resize(small, (img.shape[1], img.shape[0]), interpolation=cv2.INTER_NEAREST)

# 显示原图和马赛克处理后的图像
cv2.imshow('Original image', img)
cv2.imshow('Mosaic image', mosaic_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
'''
'''
import cv2

# 加载图像
img = cv2.imread('image1.jpg')  # 将 'input.jpg' 替换为你要处理的图像的路径

# 使用高斯滤波
blurred = cv2.GaussianBlur(img, (5, 5), 0)

# 显示原图和滤波后的图像
cv2.imshow('Original Image', img)
cv2.imshow('Gaussian Blurred Image', blurred)

# 存储高斯滤波后的图像
cv2.imwrite('blurred_image.jpg', blurred)  # 将 'blurred_image.jpg' 替换为你想要保存的文件名

cv2.waitKey(0)
cv2.destroyAllWindows()
'''
'''
import cv2
import numpy as np

# 加载图像
img = cv2.imread('blurred_image.jpg', cv2.IMREAD_GRAYSCALE)  # 将 'input.jpg' 替换为你要处理的图像的路径

# 定义拉普拉斯算子
laplacian = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], dtype=np.float32)

# 应用拉普拉斯算子
sharp_img = cv2.filter2D(img, -1, kernel=laplacian)

# 显示原图和锐化后的图像
cv2.imshow('Original Image', img)
cv2.imshow('Sharpened Image', sharp_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
'''
'''
import cv2
import numpy as np

# 读取图片
img = cv2.imread('image1.jpg')  # 将 'input.jpg' 替换为你要处理的图像的路径

rows, cols = img.shape[:2]

# 计算图像中心点
cx, cy = cols // 2, rows // 2

# 扭曲的部分为图像的中心区域
center_part = img[cy - 50:cy + 50, cx - 50:cx + 50]

# 计算仿射变换矩阵
M = np.float32([[1, 0, -50], [0, 1, -50]])

# 应用仿射变换
dst = cv2.warpAffine(center_part, M, (100, 100))

# 将扭曲后的部分替换原始图像的中心部分
img[cy - 50:cy + 50, cx - 50:cx + 50] = dst

# 显示原图和扭曲后的图像
cv2.imshow('Output', img)
cv2.waitKey()

'''
'''
import cv2
import numpy as np

def mosaic(img, block_size):
    # 对图像进行下采样
    small = cv2.resize(img, (img.shape[1] // block_size, img.shape[0] // block_size), interpolation=cv2.INTER_LINEAR)
    
    # 将小图像放大，形成马赛克效果
    result = cv2.resize(small, (img.shape[1], img.shape[0]), interpolation=cv2.INTER_NEAREST)
    
    return result

# 读取图片
img = cv2.imread('image1.jpg')  # 将 'input.jpg' 替换为你要处理的图像的路径

# 应用马赛克效果
mosaic_img = mosaic(img, 10)

# 显示原图和马赛克后的图像
cv2.imshow('Input', img)
cv2.imshow('Mosaic', mosaic_img)

cv2.waitKey()
'''
'''
import cv2
import numpy as np

# 读取图像
img = cv2.imread('image1.jpg')  # 将 'input.jpg' 替换为你要处理的图像的路径
rows, cols = img.shape[:2]

# 原图中的三个点
pts1 = np.float32([[50, 50], [200, 50], [50, 200]])

# 对应 pts1 的 pts2 是变换后的三个点
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

# 生成变换矩阵
M = cv2.getAffineTransform(pts1, pts2)

# 进行仿射变换
dst = cv2.warpAffine(img, M, (cols, rows))

# 显示原图和变换后的图像
cv2.imshow('Input', img)
cv2.imshow('Output', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
'''
import cv2
import numpy as np

# 读取图像
img = cv2.imread('image1.jpg')  # 将 'input.jpg' 替换为你要处理的图像的路径

# 图像缩放
resized_img = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)

# 获取图像的尺寸
(h, w) = resized_img.shape[:2]

# 旋转中心，角度，缩放因子
center = (w / 2, h / 2)
angle = -45
scale = 1.0

# 获取旋转矩阵
M = cv2.getRotationMatrix2D(center, angle, scale)

# 进行旋转
rotated_img = cv2.warpAffine(resized_img, M, (w, h))

# 显示原图和处理后的图像
cv2.imshow('Input', img)
cv2.imshow('Resized', resized_img)
cv2.imshow('Rotated', rotated_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
'''

import cv2
import numpy as np

# 读取图像
img = cv2.imread('image1.jpg')  # 将 'input.jpg' 替换为你要处理的图像的路径
cv2.imshow('Input', img)
'''
rows, cols = img.shape[:2]

# 原图中的四个点，这四个点构成一个矩形
pts1 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])

# 对应 pts1 的 pts2 是变换后的四个点
pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])

# 生成变换矩阵
M = cv2.getPerspectiveTransform(pts1, pts2)

# 进行剪切影射
dst = cv2.warpPerspective(img, M, (cols, rows))
'''
'''
# 显示原图和变换后的图像
cv2.imshow('Input', img)
cv2.imshow('Output', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
