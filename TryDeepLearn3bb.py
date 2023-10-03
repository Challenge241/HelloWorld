# -*- coding: utf-8 -*-
"""
Created on Mon May 29 20:16:03 2023

@author: Lenovo
"""

import paddle
import paddle.inference as inference
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def load_image(file):
    im = Image.open(file)
    im = im.resize((32, 32), Image.Resampling.LANCZOS)
    im = np.array(im).astype(np.float32)
    im = im.transpose((2, 0, 1))
    im = im / 255.0
    im = np.expand_dims(im, axis=0)
    return im

model_save_dir = "./catdog.inference.model"

# 创建预测器
config = paddle.inference.Config(model_save_dir)
predictor = paddle.inference.create_predictor(config)

# 预测单个图片
img_path = 'C:/Users/Lenovo/Desktop/data/data/dog1.png'
img = Image.open(img_path)
plt.imshow(img)
plt.show()

img = load_image(img_path)
input_names = predictor.get_input_names()
input_handle = predictor.get_input_handle(input_names[0])
input_handle.copy_from_cpu(img)

predictor.run()

output_names = predictor.get_output_names()
output_handle = predictor.get_output_handle(output_names[0])

output_data = output_handle.copy_to_cpu()

label_list = ["cat", "dog"]
print("infer results: %s" % label_list[np.argmax(output_data[0])])
