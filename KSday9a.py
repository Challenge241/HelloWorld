# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 14:14:40 2023

@author: Lenovo
"""

# 导入os库，用于处理文件和目录
import os
# 导入numpy库，用于处理数组和矩阵
import numpy as np
# 导入OpenCV库，用于处理图像和视频
import cv2 as cv

# 定义load_info函数，用于从face目录中读取图像并进行预处理
def load_info():
    # 读取face目录中的所有文件
    listdir = os.listdir('face')
    # 输出所有读取的文件
    print(listdir)
    # 定义faces列表，用于存储所有读取的图像
    faces = []
    # 定义target列表，用于存储图像对应的标签
    target = []
    # 遍历所有文件
    for index, dir in enumerate(listdir):
        for i in os.listdir('face/{}'.format(dir)):
            # 读取图像，并转换为灰度图
            gray = cv.imread('face/{}/{}'.format(dir, i))
            # 将图像转换为二维数组
            gray1 = gray[:, :, 0] 
            # 将图像的大小调整为64x64
            gray2 = cv.resize(gray1, dsize=(64, 64))
            # 将处理后的图像添加到faces列表中
            faces.append(gray2)
            # 将图像的标签添加到target列表中
            target.append(index)
    # 将faces和target列表转换为numpy数组
    faces = np.asarray(faces)
    target = np.asarray(target)
    # 返回faces、target和listdir
    return faces, target, listdir

# 定义split_data函数，用于将数据集划分为训练集和测试集
def split_data( faces, target):
    # 生成一个长度为faces的长度的数组
    index = np.arange( len(faces) )
    # 打乱这个数组的顺序
    np.random.shuffle( index )
    # 将数据集和标签集根据index的位置进行打乱
    faces = faces[index]
    target = target[index]
    # 拆分数据集，80%作为训练集，20%作为测试集
    x_train = faces[:149]
    y_train = target[:149]
    x_test = faces[149:]
    y_test = target[149:]
    # 返回训练集和测试集
    return  x_train, y_train, x_test, y_test

# 如果当前脚本是主程序，则执行以下代码
if __name__ == '__main__':
    # 提取数据
    faces, target, names = load_info()
    # 切分数据，80%作为训练集，20%作为测试集
    x_train, y_train, x_test, y_test = split_data(  faces, target  )
    # 创建一个EigenFace人脸识别器对象
    face_recognizer = cv.face.EigenFaceRecognizer.create()
    # 使用训练集进行训练
    face_recognizer.train( x_train, y_train)
    # 使用测试集进行测试
    for x in x_test:
        # 使用识别器进行预测，得到预测的标签和置信度
        y_, confidence = face_recognizer.predict(x)
        # 如果置信度小于500，则认为预测结果较好
        if confidence<500:
            print('置信度比较好：', names[y_], confidence,  )
        else:
            # 否则，认为预测结果较差
            print('置信度偏高，效果比较差:', names[y_], confidence,  )
