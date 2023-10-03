# -*- coding: utf-8 -*-
"""
Created on Mon May 29 15:39:22 2023

@author: Lenovo
"""

import paddle.fluid as fluid
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


model_save_dir = "./catdog.inference.model"

use_cuda = False
place = fluid.CUDAPlace(0) if use_cuda else fluid.CPUPlace()

infer_exe = fluid.Executor(place)
inference_scope = fluid.core.Scope()

def load_image(file):
    # 打开图片
    im = Image.open(file)
    # 将图片调整为跟训练数据一样的大小  32*32，设定ANTIALIAS，即抗锯齿.resize是缩放
    im = im.resize((32, 32), Image.ANTIALIAS)
    # 建立图片矩阵 类型为float32
    im = np.array(im).astype(np.float32)
    # 矩阵转置
    im = im.transpose((2, 0, 1))
    # 将像素值从【0-255】转换为【0-1】
    im = im / 255.0
    # print(im)
    im = np.expand_dims(im, axis=0)
    # 保持和之前输入image维度一致
    print('im_shape的维度：', im.shape)
    return im




with fluid.scope_guard(inference_scope):
    # 从指定目录中加载 推理model(inference model)
    [inference_program,  # 预测用的program
# 是一个str列表，它包含需要在推理 Program 中提供数据的变量的名称。
     feed_target_names,  
# fetch_targets：是一个 Variable 列表，从中我们可以得到推断结果。
     fetch_targets] = fluid.io.load_inference_model(model_save_dir,  
                                                    infer_exe)  
# infer_exe: 运行 inference model的 executor

    infer_path = 'C:/Users/Lenovo/Desktop/data/data/dog1.png'
    img = Image.open(infer_path)
    plt.imshow(img)
    plt.show()

    img = load_image(infer_path)

    results = infer_exe.run(inference_program,  # 运行预测程序
                            feed={feed_target_names[0]: img},  # 喂入要预测的img
                            fetch_list=fetch_targets)  # 得到推测结果
    print('results', results)
    label_list = [
        "airplane", "automobile", "bird", "cat", "deer", "dog", "frog", "horse",
        "ship", "truck"
    ]
    print("infer results: %s" % label_list[np.argmax(results[0])])
