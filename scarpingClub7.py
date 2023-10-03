# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 10:38:51 2023

@author: Lenovo
"""



import requests
import json
import time
url = 'https://scrapingclub.com/exercise/ajaxdetail_cookie/?token=NLCB0YXBSO'  # 替换为实际的Ajax请求URL
#设置合适的User-Agent
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}
response = requests.get(url, headers=headers)
#处理Cookies
session = requests.Session()
session.get(url)  # 这将获取和处理Cookies
response = session.get(url)  # 使用相同的会话发送请求
#处理重定向
response = requests.get(url)  # 禁止自动重定向
if response.status_code == 302:  # 处理特定的重定向状态码
    redirect_url = response.headers['Location']
    response = requests.get(redirect_url)
#添加延迟
time.sleep(0.5)
#检查
print("response.status_code:"+str(response.status_code))
print("response.headers:"+str(response.headers))
print("response.content:"+str(response.content))
print("response.text:"+response.text)
'''
data = response.json()

# 提取产品详细信息
title = data['title']  # 替换为实际的标题键路径
description = data['description']  # 替换为实际的描述键路径
price = data['price']  # 替换为实际的价格键路径

# 打印产品详细信息
print('Title:', title)
print('Description:', description)
print('Price:', price)
'''