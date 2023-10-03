# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 20:04:10 2023

@author: Lenovo
"""

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


# 创建driver对象
driver = webdriver.Chrome()

# driver = webdriver.Edge()
# webdriver.Firefox()
# 设置浏览器的窗口最大化
driver.maximize_window()
# 访问网址
driver.get( 'https://www.4khd.com' )


time.sleep(3)

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



login_url = 'https://www.4khd.com/'

with requests.Session() as s:
    url = login_url
    r = s.get(url)
    r = s.post(url)

    # After this, you can use 's' to fetch URLs as a logged in user


download_images(login_url, folder)

'''
ProxyError: HTTPSConnectionPool(host='www.4khd.com', port=443): 
    Max retries exceeded with url: / (Caused by ProxyError('Cannot connect to proxy.', 
    ConnectionResetError(10054, '远程主机强迫关闭了一个现有的连接。', None, 10054, None)))
'''