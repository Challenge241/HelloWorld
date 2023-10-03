# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 16:16:35 2023

@author: Lenovo
"""
import requests
from bs4 import BeautifulSoup
import os

# 目标网页的URL，这里只做示例，使用了一个公开的、允许爬取的网址
url = "https://www.example.com"

# 创建一个新的请求会话，获取目标网页的内容
response = requests.get(url)
response.raise_for_status()  # 如果请求失败，这将引发一个异常

# 将网页内容解析为HTML
soup = BeautifulSoup(response.text, 'html.parser')

# 在HTML中查找所有的<img>标签
img_tags = soup.find_all('img')

# 创建一个文件夹来保存下载的图片
os.makedirs('D:\\coser', exist_ok=True)

# 遍历每个<img>标签
for tag in img_tags:
    # 获取标签的'src'属性，即图片的URL
    img_url = tag.get('src')

    # 只处理有效的图片URL
    if img_url is not None and 'http' in img_url:
        # 从URL中获取图片的名字
        img_name = os.path.basename(img_url)

        # 向URL发送一个请求，下载图片
        img_response = requests.get(img_url)
        img_response.raise_for_status()  # 如果请求失败，这将引发一个异常

        # 将图片保存到本地
        with open(os.path.join('D:\\coser', img_name), 'wb') as img_file:
            img_file.write(img_response.content)

