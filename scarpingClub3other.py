# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 11:23:56 2023

@author: Lenovo
"""

#Exercise Page=https://scrapingclub.com/exercise/list_basic/
import requests
from bs4 import BeautifulSoup

base_url = "https://scrapingclub.com/exercise/list_basic/"

def singlePage(url):
    # 发送GET请求获取页面内容
    r = requests.get(base_url)
    data = r.text
    
    # 使用BeautifulSoup解析页面内容
    soup = BeautifulSoup(data, 'lxml')
    
    # 提取商品信息
    items = soup.find_all("div", class_="col-lg-4 col-md-6 mb-4")
    for i in items:
        i = i.find("div", class_="card-body")
        # 打印商品名称和价格
        print("Item Name: {}\nItem Price: {}".format(i.h4.text.lstrip('\n'), i.h5.text))

# 获取所有产品页面的链接
r = requests.get(base_url)
soup = BeautifulSoup(r.text, 'lxml')
pages = soup.find_all("a", class_="page-link")
pagelist = []
for p in pages:
    isvalid = p.text if p.text.isdigit() else None
    if isvalid:
        pagelist.append(p.get('href'))

# 遍历所有页面
for i in pagelist:
    url = base_url + i
    singlePage(base_url)
