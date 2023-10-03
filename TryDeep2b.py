# -*- coding: utf-8 -*-
"""
Created on Tue May 16 11:28:21 2023

@author: Lenovo
"""

# 导入必要的包
import paddle
import paddle.dataset.imdb as imdb
import paddle.fluid as fluid
import numpy as np

paddle.enable_static()

word_dict = imdb.word_dict()
use_cuda = False
place = fluid.CUDAPlace(0) if use_cuda else fluid.CPUPlace()
model_save_dir = "./emotionclassify.inference.model"


# 我们先定义三个句子，第一句是中性的，第二句偏向正面，第三句偏向负面。然后把这些句子读取到一个列表中。
# 定义预测数据
reviews_str = ['read the book forget the movie', 'this is a great movie', 'this is very bad']
# 把每个句子拆成一个个单词
reviews = [c.split() for c in reviews_str]
# 然后把句子转换成编码，根据数据集的字典，把句子中的单词转换成对应标签。
# 获取结束符号的标签
UNK = word_dict['<unk>']
# 获取每句话对应的标签
lod = []
for c in reviews:
    # 需要把单词进行字符串编码转换
    lod.append(np.array([word_dict.get(words.encode('utf-8'), UNK) for words in c]).astype(np.int64))
# 获取每句话的单词数量
base_shape = [[len(c) for c in lod]]
# 生成预测数据
tensor_words = fluid.create_lod_tensor(lod, base_shape, place)
infer_exe = fluid.Executor(place)    #创建推测用的executor
inference_scope = fluid.core.Scope() #Scope指定作用域
with fluid.scope_guard(inference_scope):#修改全局/默认作用域（scope）, 运行时中的所有变量都将分配给新的scope。
    #从指定目录中加载 推理model(inference model)
    [inference_program,        #推理的program
     feed_target_names,        #str列表，包含需要在推理program中提供数据的变量名称
     fetch_targets] = fluid.io.load_inference_model(model_save_dir, infer_exe)                                                
#fetch_targets: 推断结果，model_save_dir:模型训练路径
#infer_exe: 运行 inference model的 executor
    print("完成预测程序加载")
    results = infer_exe.run(inference_program,                         #运行预测程序
                          feed={feed_target_names[0]: tensor_words},#喂入要预测的x值
                          fetch_list=fetch_targets)                 #得到推测结果 
    print("完成预测")
    # 打印每句话的正负面概率
    for i, r in enumerate(results[0]):
        print("\'%s\'的预测结果为：正面概率为：%0.5f，负面概率为：%0.5f" % (reviews_str[i], r[0], r[1]))
