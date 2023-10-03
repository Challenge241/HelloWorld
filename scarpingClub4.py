# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 10:31:01 2023

@author: Lenovo
"""


import requests

headers = {
    'User-Agent': 'Mozilla/5.0',  # 这只是一个例子，请使用实际的请求头
    # 其他请求头...
}

response = requests.get('https://scrapingclub.com/exercise/ajaxdetail/', headers=headers)  # 或者requests.post()对于POST请求
data = response.json()  # Ajax通常返回JSON数据
print(data)