# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 19:37:33 2023

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
image_counter = 1

def save_imgs(title,src):
    global image_counter
    #让图片的标题作为图片的名称
    filename=title
    filename = filename.replace("?", "_").replace("%", "_")#处理非法字符
    # 添加序号到文件名前面
    filename = str(image_counter) + "_" + filename
    filename = os.path.join(folder, filename)
    # 下载图片
    with open(filename, 'wb') as f:
        f.write(requests.get(src).content)
    print('Downloaded', filename)
    image_counter+=1
    # 打开原始图片
    img = Image.open(filename)
    # 创建新的文件名，扩展名为.png
    new_filename = os.path.splitext(filename)[0] + ".png"
    #转换图片格式并保存
    img.save(new_filename, 'PNG')    

def get_html(url):
    # 访问网址
    driver.get(url)
    time.sleep(0.3)
    # 向下滑动   # 可以执行js代码的方法
    for i in range(2000):
        driver.execute_script('window.scrollBy(0, 15)')
    time.sleep(0.5)
    # 等待这个浏览器充分加载完毕之后
    html = driver.page_source
    #print( html )
    return html
    
def scrap_images(url, folder):
    global image_counter    
    html=get_html(url)
    soup = BeautifulSoup( html, 'html.parser')
    groups = soup.find_all('div',class_='wp-block-template-part')
    for group in groups:
        #获取封面图片的src
        image=group.find('img')
        src = image.get('src')
        #获取图片的标题
        title=group.find('h2').text.strip()
        print('title:'+title)
        save_imgs(title,src)
        #获取图片详情页链接，换句话说，我们下的图片其实是图集的封面，我们要进入图集，下图集的其他图
        a_tag=group.find('a')
        if a_tag is not None and 'href' in a_tag.attrs:
            link = a_tag['href']
            print("link:"+link)
        #访问详情页链接,也就是图集的首页
        html_first=get_html(link)
        soup_first = BeautifulSoup( html_first, 'html.parser')
        #查看图集有几页
        ul_tag=soup_first.find('ul',class_='page-links')
        if ul_tag is not None:
            li_tags = ul_tag.find_all('li')
            num_of_li = len(li_tags)
        #如果没有该标签说明只有1页
        else:
            num_of_li=1 
        print(num_of_li)
        #依次访问图集各页链接
        for i in range(1,num_of_li+1):
            link_detail=link+f"/{i}"
            html_detail=get_html(link_detail)
            soup_detail = BeautifulSoup( html_detail, 'html.parser')
            groups_detail=soup_detail.find_all('figure',class_='wp-block-image size-large')
            for group_detail in groups_detail:
                #获取图集里的图片的src
                image_detail=group_detail.find('img')
                src_detail = image_detail.get('src')
                save_imgs(title, src_detail)
            
        print("Try")
    time.sleep(0.5)
    print("OK")
    
# 确保文件夹存在
folder = 'D:\\PaQv\\PaQvTry'
if not os.path.exists(folder):
    os.makedirs(folder)
    # After this, you can use 's' to fetch URLs as a logged in user
# 页面的URL
base_url = "https://www.4khd.com/?query-3-page={}&cst"
for page in range(5, 6):
    scrap_images(base_url.format(page), folder)
time.sleep(12)