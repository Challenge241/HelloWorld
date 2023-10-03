# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 10:14:27 2023

@author: Lenovo
"""

'''
import requests

url = "http://www.4399.com"  # 这里换成你的目标网页
response = requests.get(url)

print(response.status_code)  # 输出 HTTP 状态码
print(response.text)  # 输出网页内容
'''

''' 为了在请求中使用代理，你可以传递一个proxies参数给get或者post方法'''

'''
import requests

proxies = {
  'http': 'http://10.10.1.10:3128',
  'https': 'http://10.10.1.10:1080',
}

response = requests.get('http://www.example.com', proxies=proxies)

'''

'''
from lxml import html
import requests

url = 'http://www.4399.com'  # 目标网页
response = requests.get(url)
tree = html.fromstring(response.content)

# xpath 表达式，获取所有图片的链接
image_urls = tree.xpath('//img/@src')  

for image_url in image_urls:
    print(image_url)
    
'''

'''
from bs4 import BeautifulSoup
import requests

url = 'http://www.4399.com'  # 目标网页
response = requests.get(url)
soup = BeautifulSoup(response.content, 'lxml')  # 'lxml' 是解析器

# 使用 BeautifulSoup 的 find_all 方法获取所有图片
images = soup.find_all('img')

for image in images:
    print(image.get('src'))  # 打印图片链接
    
'''

'''
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def download_images(url, folder):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        images = soup.find_all('img')
        for image in images:
            src = image.get('src')
            # 如果链接是相对链接，将其转换为绝对链接
            src = urljoin(url, src)
            # 获取文件名
            filename = os.path.join(folder, src.split('/')[-1])
            # 下载图片
            with open(filename, 'wb') as f:
                f.write(requests.get(src).content)
            print('Downloaded', filename)
    except Exception as e:
        print('Error:', e)

download_images('http://www.4399.com', 'images')
'''

import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def download_images(url, folder):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        images = soup.find_all('img')
        for image in images:
            src = image.get('src')
            # 如果链接是相对链接，将其转换为绝对链接
            src = urljoin(url, src)
            # 获取文件名
            filename = os.path.join(folder, src.split('/')[-1])
            # 下载图片
            with open(filename, 'wb') as f:
                f.write(requests.get(src).content)
            print('Downloaded', filename)
    except Exception as e:
        print('Error:', e)

# 确保文件夹存在
folder = 'D:\\PaQv'
if not os.path.exists(folder):
    os.makedirs(folder)

download_images('http://www.4399.com', folder)
