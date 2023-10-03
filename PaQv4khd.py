# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 22:17:49 2023

@author: Lenovo
"""

import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
chrome_options = Options()
#禁用javescript
chrome_options.add_experimental_option("prefs", {'profile.managed_default_content_settings.javascript': 2})
# 创建 WebDriver 实例（这里使用 Chrome 浏览器）
driver = webdriver.Chrome( options=chrome_options)
def download_images(url, folder):    
    # 访问网址
    driver.get(url)
    time.sleep(1)
    # 在循环外部，初始化序列号
    image_counter = 1
    # 向下滑动   # 可以执行js代码的方法
    for i in range(1000):
        driver.execute_script('window.scrollBy(0, 5)')
    time.sleep(1)
    # 等待这个浏览器充分加载完毕之后
    html = driver.page_source
    #print( html )
    soup = BeautifulSoup( html, 'html.parser')
    images = soup.find_all('img')
    for image in images:
        src = image.get('src')
        # 如果链接是相对链接，将其转换为绝对链接
        #src = urljoin(url, src)
        # 获取文件名
        filename = src.split('/')[-1]
        filename = filename.replace("?", "_").replace("%", "_")
        # 改变文件扩展名为.png
        #filename = os.path.splitext(filename)[0] + ".png"
        # 添加序号到文件名前面
        filename = str(image_counter) + "_" + filename
        filename = os.path.join(folder, filename)
        # 下载图片
        with open(filename, 'wb') as f:
            f.write(requests.get(src).content)
        print('Downloaded', filename)
        image_counter += 1
        # 打开原始图片
        img = Image.open(filename)
        # 创建新的文件名，扩展名为.png
        new_filename = os.path.splitext(filename)[0] + ".png"
        #转换图片格式并保存
        img.save(new_filename, 'PNG')                
    time.sleep(60)
    print("OK")
# 确保文件夹存在
folder = 'D:\\PaQv'
if not os.path.exists(folder):
    os.makedirs(folder)
    # After this, you can use 's' to fetch URLs as a logged in user
    
download_images('https://www.4khd.com', folder)
