# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 10:19:31 2023

@author: Lenovo
"""

import requests
import json

# 发送Ajax请求获取产品信息
url = 'https://scrapingclub.com/exercise/ajaxdetail/'  # 替换为实际的Ajax请求URL
response = requests.get(url)
data = response.json()

# 提取产品详细信息
title = data['title']  # 替换为实际的标题键路径
description = data['description']  # 替换为实际的描述键路径
price = data['price']  # 替换为实际的价格键路径

# 打印产品详细信息
print('Title:', title)
print('Description:', description)
print('Price:', price)
