# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 10:40:34 2023

@author: Lenovo
"""
'''
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# 页面的URL
base_url = "https://scrapingclub.com/exercise/list_basic/?page=1"

# 发送GET请求
response = requests.get(base_url)

# 解析HTML文档
soup = BeautifulSoup(response.text, 'html.parser')

# 获取所有商品卡片
cards = soup.find_all('div', class_='card')

#print(cards)

# 遍历每个卡片
for card in cards:
    # 在当前卡片中找到链接
    link = card.find('a')
    print(link)
    # 构造完整的商品链接
    product_url = urljoin(base_url, link['href'])
    print("product_url:"+product_url)
    # 访问商品详情页
    response = requests.get(product_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # 获取商品标题
    product_title_element = soup.find('h2')
    if product_title_element is not None:
        product_title = product_title_element.text.strip()
    else:
        product_title = None

    # 获取商品价格
    product_price_element = soup.find('h4')
    if product_price_element is not None:
        product_price = product_price_element.text.strip()
    else:
        product_price = None

    # 获取商品描述
    product_description_element = soup.find('p')
    if product_description_element is not None:
        product_description = product_description_element.text.strip()
    else:
        product_description = None

    print(f'商品标题：{product_title}，价格：{product_price}，描述：{product_description}')
'''
'''
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# 页面的URL
base_url = "https://scrapingclub.com/exercise/list_basic/?page=1"

# 发送GET请求
response = requests.get(base_url)

# 解析HTML文档
soup = BeautifulSoup(response.text, 'html.parser')

# 获取所有商品卡片
cards = soup.find_all('div', class_='card')

# 遍历每个卡片
for card in cards:
    # 在当前卡片中找到链接
    a_tag = card.find('a')
    if a_tag is not None and 'href' in a_tag.attrs:
        link = a_tag['href']

        # 构造完整的商品链接
        product_url = urljoin(base_url, link)
        print("product_url:"+ product_url)
        # 访问商品详情页
        response = requests.get(product_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # 获取商品标题
        product_title_element = soup.find('h2')
        if product_title_element is not None:
            product_title = product_title_element.text.strip()
        else:
            product_title = None

        # 获取商品价格
        product_price_element = soup.find('h4')
        if product_price_element is not None:
            product_price = product_price_element.text.strip()
        else:
            product_price = None

        # 获取商品描述
        product_description_element = soup.find('p')
        if product_description_element is not None:
            product_description = product_description_element.text.strip()
        else:
            product_description = None

        print(f'商品标题：{product_title}，价格：{product_price}，描述：{product_description}')
'''

'''
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
    # 获取商品标题
    product_title_element = card.find('h3', class_='card-body')
    if product_title_element is not None:
        product_title = product_title_element.text.strip()
    else:
        product_title = None

    # 获取商品价格
    product_price_element = card.find('h4', class_='card-body')
    if product_price_element is not None:
        product_price = product_price_element.text.strip()
    else:
        product_price = None

    # 获取商品描述
    product_description_element = card.find('p', class_='card-body')
    if product_description_element is not None:
        product_description = product_description_element.text.strip()
    else:
        product_description = None

    print(f'商品标题：{product_title}，价格：{product_price}，描述：{product_description}')
'''