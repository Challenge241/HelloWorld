# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 11:22:58 2023

@author: Lenovo
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd

# 通过修改URL中的页码来遍历每一页
all_data = []  # 初始化一个空的列表来存储数据

for i in range(1, 51):  # 假设有50页
    url = f"http://books.toscrape.com/catalogue/category/books/default_15/page-{i}.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # 找到每本书的标题和价格
    books = soup.find_all('li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')
    for book in books:
        title = book.find('h3').find('a')['title']
        price = book.find('p', class_='price_color').text

        # 添加到列表中
        all_data.append({"Book Title": title, "Price": price})

# 将列表转换为DataFrame
data = pd.DataFrame(all_data)

# 将数据保存到CSV文件中
data.to_csv("books_data.csv", index=False)
