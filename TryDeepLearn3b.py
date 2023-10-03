# -*- coding: utf-8 -*-
"""
Created on Mon May 29 20:00:53 2023

@author: Lenovo
"""


import paddle.fluid as fluid
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def load_image(file):
    # 打开图片
    im = Image.open(file)
    # 将图片调整为跟训练数据一样的大小  32*32，设定ANTIALIAS，即抗锯齿.resize是缩放
    im = im.resize((32, 32), Image.LANCZOS)
    # 建立图片矩阵 类型为float32
    im = np.array(im).astype(np.float32)
    # 矩阵转置
    im = im.transpose((2, 0, 1))
    # 将像素值从【0-255】转换为【0-1】)})
    im = im / 255.0
    # print(im) 显示图片矩阵
    # 保持和之前输入image维度一致
    im = np.expand_dims(im, axis=0)
    return im

model_save_dir = "./catdog.inference.model"

# 创建执行器，CPU运行速度比较慢，可以用GPU运行，使用GPU需要在终端输入：export CUDA_VISIBLE_DEVICES=0
place = fluid.CPUPlace()
exe = fluid.Executor(place)
exe.run(fluid.default_startup_program())


# 从模型中获取预测程序，输入数据名称列表，分类器
[infer_program, feeded_var_names, target_var] = fluid.io.load_inference_model(dirname=model_save_dir, executor=exe)

# 预测单个图片
img_path = 'dog.png'
img = Image.open(img_path)
plt.imshow(img)
plt.show()

img = load_image(img_path)
result = exe.run(program=infer_program,
                 feed={feeded_var_names[0]: img},
                 fetch_list=target_var)

# 显示图片并输出最可能的情感标签
label_list = ["cat", "dog"]
print("infer results: %s" % label_list[np.argmax(result[0])])