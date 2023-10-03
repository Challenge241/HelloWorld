# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 22:54:05 2023

@author: Lenovo
"""

import os
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from PIL import Image

chrome_options = Options()
#禁用javescript
chrome_options.add_experimental_option("prefs", {'profile.managed_default_content_settings.javascript': 2})
# 创建 WebDriver 实例（这里使用 Chrome 浏览器）
driver = webdriver.Chrome( options=chrome_options)
# 在循环外部，初始化序列号
def save_imgs(title, src, subfolder,image_counter):
    filename = title
    filename = filename.replace("?", "_").replace("%", "_")  # 处理非法字符
    filename = str(image_counter) + "_" + filename
    filename = os.path.join(subfolder, filename)  # 将图片保存在子文件夹中
    with open(filename, 'wb') as f:
        f.write(requests.get(src).content)
    print('Downloaded', filename)
    img = Image.open(filename)
    new_filename = os.path.splitext(filename)[0] + ".png"
    img.save(new_filename, 'PNG')
    
def get_html(url):
    # 访问网址
    driver.get(url)
    time.sleep(0.3)
    # 向下滑动   # 可以执行js代码的方法
    for i in range(1500):
        driver.execute_script('window.scrollBy(0, 20)')
    time.sleep(0.5)
    # 等待这个浏览器充分加载完毕之后
    html = driver.page_source
    #print( html )
    return html

def scrap_images(url, folder):
    global image_counter
    html = get_html(url)
    soup = BeautifulSoup(html, 'html.parser')
    groups = soup.find_all('div', class_='wp-block-template-part')
    for group in groups:
        image = group.find('img')
        src = image.get('src')
        title = group.find('h2').text.strip()
        print('title:' + title)
        # 创建一个新的子文件夹，它的名字是由图集的标题决定的
        subfolder = os.path.join(folder, title)
        if not os.path.exists(subfolder):
            os.makedirs(subfolder)
        image_counter=1
        save_imgs(title, src, subfolder,image_counter)  # 将子文件夹的名字传递给save_imgs函数
        image_counter+=1
        a_tag = group.find('a')
        if a_tag is not None and 'href' in a_tag.attrs:
            link = a_tag['href']
            print("link:" + link)
        html_first = get_html(link)
        soup_first = BeautifulSoup(html_first, 'html.parser')
        ul_tag = soup_first.find('ul', class_='page-links')
        if ul_tag is not None:
            li_tags = ul_tag.find_all('li')
            num_of_li = len(li_tags)
        else:
            num_of_li = 1
        print(num_of_li)
        for i in range(1, num_of_li + 1):
            link_detail = link + f"/{i}"
            html_detail = get_html(link_detail)
            soup_detail = BeautifulSoup(html_detail, 'html.parser')
            groups_detail = soup_detail.find_all('figure', class_='wp-block-image size-large')
            for group_detail in groups_detail:
                image_detail = group_detail.find('img')
                src_detail = image_detail.get('src')
                save_imgs(title, src_detail, subfolder,image_counter)  # 将子文件夹的名字传递给save_imgs函数
                image_counter+=1
        print("Try")
    time.sleep(0.5)
    print("OK")


folder = 'E:\\PaQv4khd'
if not os.path.exists(folder):
    os.makedirs(folder)
base_url= "https://www.4khd.com/?query-3-page={}&cst"
for page in range(12, 255):
    scrap_images(base_url.format(page), folder)
time.sleep(12)
