# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 16:34:29 2023

@author: Lenovo
"""

import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import shutil

# 定义HTTP标头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}
# 页面的URL
base_url = "https://scrapingclub.com/exercise/list_basic/?page={}"
# 在循环外部，初始化序列号
image_counter = 1
# 遍历每个页面
for page in range(1, 8):
    # 发送GET请求
    response = requests.get(base_url.format(page), headers=headers)
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
            print("link:"+link)
            if link=="/exercise/detail_basic/":
                continue

            # 构造完整的商品链接
            product_url = urljoin(base_url, link)
            print("product_url:"+ product_url)

            # 访问商品详情页
            response = requests.get(product_url)
            soup = BeautifulSoup(response.text, 'html.parser')
            # 获取商品详情页的卡片
            card_detaile = soup.find('div', class_='card mt-4 my-4')
            #获取商品名称
            product_title_element =  card_detaile.find('h3', class_='card-title')
            if product_title_element is not None:
                product_title = product_title_element.text.strip()
            else:
                product_title = None

            # 获取商品价格
            product_price_element =  card_detaile.find('h4')
            if product_price_element is not None:
                product_price = product_price_element.text.strip()
            else:
                product_price = None

            # 获取商品描述
            product_description_element =  card_detaile.find('p', class_='card-text')
            if product_description_element is not None:
                product_description = product_description_element.text.strip()
            else:
                product_description = None

            print(f'商品标题：{product_title}，价格：{product_price}，描述：{product_description}')
            
            # 获取商品图片链接
            img_element = card.find('img')
            if img_element is not None:
                img_url = urljoin(product_url, img_element['src'])
                # 请求图片内容
                img_response = requests.get(img_url, stream=True)
                # 将标题和价格用于图片名称，并去掉不合法的文件名字符
                invalid_chars = '\\/:*?"<>|'
                product_title = ''.join(c for c in product_title if c not in invalid_chars)
                product_price = ''.join(c for c in product_price if c not in invalid_chars)
                # 图片文件名
                img_filename = f"D:\\scarpingClubPic\\img{image_counter}_{product_title}_{product_price}.jpg"
                # 保存图片到本地
                with open(img_filename, 'wb') as out_file:
                    shutil.copyfileobj(img_response.raw, out_file)
                print(f"成功保存图片 {img_filename}")
                
                # 描述文件名
                txt_filename = f"D:\\scarpingClubPic\\img{image_counter}_{product_title}_{product_price}.txt"
                # 保存商品描述到本地
                with open(txt_filename, 'w',encoding='utf-8') as out_file:
                    out_file.write(product_description)
                print(f"成功保存商品描述 {txt_filename}")

                image_counter += 1
            else:
                print("未能获得商品图片链接或者该商品没有图片")
