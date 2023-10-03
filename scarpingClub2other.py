# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 11:26:33 2023

@author: Lenovo
"""

#Exercise Page=https://scrapingclub.com/exercise/detail_json/
import requests
import re
import json
from bs4 import BeautifulSoup

url = "https://scrapingclub.com/exercise/detail_json/"

# 发送GET请求获取页面内容
r = requests.get(url)
data = r.text

# 使用BeautifulSoup解析页面内容
soup = BeautifulSoup(data, "lxml")

# 在页面中查找包含目标数据的<script>标签
script = soup.find("script", string=re.compile('var obj ='))

# 使用正则表达式从<script>标签的内容中提取JSON数据
json_text = re.search(r'^\s*var obj\s*=\s*({.*?})\s*;\s*$', script.string, flags=re.DOTALL | re.MULTILINE).group(1)

# 清理JSON数据中的一些无效部分
json_text = json_text.replace("\"/static/img/\" + ", "")
json_text = json_text.replace("\"96230-C\" + ", "")

# 解析JSON数据
parsed = json.loads(json_text)

# 打印提取的数据
print("Item Name: {}\nItem Price: {}\nItem Description: {}".format(parsed['title'], parsed['price'], parsed['description']))
