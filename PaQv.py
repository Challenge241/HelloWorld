# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 18:13:15 2023

@author: Lenovo
"""

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
folder = 'D:\\PaQv4399'
if not os.path.exists(folder):
    os.makedirs(folder)

    # After this, you can use 's' to fetch URLs as a logged in user


download_images('https://www.google.com/', folder)
