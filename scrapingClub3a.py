# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 09:24:14 2023

@author: Lenovo
"""

import requests
from bs4 import BeautifulSoup

# 页面的URL
url = "https://scrapingclub.com/exercise/list_basic/?page=1"

# 发送GET请求
response = requests.get(url)

# 解析HTML文档
soup = BeautifulSoup(response.text, 'html.parser')

# 获取所有商品卡片
cards = soup.find_all('div', class_='card')

# 遍历每个商品卡片
for card in cards:
    print(card)
    print("------")
    # 获取商品名称
    product_name_element = card.find('h4', class_='card-title')
    if product_name_element is not None:
        product_name = product_name_element.text.strip()
    else:
        product_name = None

    # 获取商品价格
    product_price_element = card.find('h5')
    if product_price_element is not None:
        product_price = product_price_element.text.strip()
    else:
        product_price = None
        
    if(product_price != None and product_name != None):
        print(f'商品名称：{product_name}，价格：{product_price}')
