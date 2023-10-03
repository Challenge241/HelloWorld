# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 11:11:07 2023

@author: Lenovo
"""

import os  # 提供了很多与操作系统交互的功能
import requests  # 网络请求库
from bs4 import BeautifulSoup  # 用于网页解析，即从网页中抓取数据
from selenium import webdriver  # 用于自动化网页操作，包括加载网页、搜索和点击按钮等
import time  # 提供时间相关的功能
from selenium.webdriver.chrome.options import Options  # 用于配置Chrome浏览器的选项
from PIL import Image  # 用于处理图像的库
import random
from requests.exceptions import RequestException
chrome_options = Options()  # 初始化Chrome浏览器选项
chrome_options.add_experimental_option("prefs", {'profile.managed_default_content_settings.javascript': 2})  # 禁用JavaScript
driver = webdriver.Chrome( options=chrome_options)  # 创建一个Chrome浏览器实例
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
    "Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0",
    "Mozilla/4.0(compatible;MSIE8.0;WindowsNT6.0;Trident/4.0)",
    "Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1",
    "Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1",
    "Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11",
    "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Maxthon2.0)",
    "Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11",
    "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TencentTraveler4.0)",
    "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TheWorld)",
    "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Trident/4.0;SE2.XMetaSr1.0;SE2.XMetaSr1.0;.NETCLR2.0.50727;SE2.XMetaSr1.0",
    "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;360SE)"
]


def get_random_user_agent(user_agents):
    return random.choice(user_agents)



# 在循环外部，初始化序列号
def save_imgs(title, src, subfolder,image_counter):  # 定义一个函数，用于保存图片
    retry_count=0
    retry_limit=5
    filename = title  # 图片的文件名
    filename = filename.replace("?", "_").replace("%", "_")  # 处理非法字符
    filename = str(image_counter) + "_" + filename  # 拼接图片文件名
    filename = os.path.join(subfolder, filename)  # 构造图片的完整路径
    while retry_count < retry_limit:
        try:
            random_user_agent=get_random_user_agent(user_agents)
            headers = {
                "User-Agent": random_user_agent
                }
            print("?a")
            response = requests.get(src,headers = headers)
            #response = requests.get(src)
            time.sleep(random.random())
            break
            print("?b")
        except RequestException as e:
            print(f"Error occurred while fetching the URL: {e}")
            retry_count += 1
            time.sleep(random.random())
    with open(filename, 'wb') as f:  # 以二进制写模式打开文件
        f.write(response.content)  # 下载图片并保存到文件中
    print('Downloaded', filename)  # 输出下载成功的消息
    img = Image.open(filename)  # 用PIL库打开图片
    new_filename = os.path.splitext(filename)[0] + ".png"  # 构造新的文件名
    img.save(new_filename, 'PNG')  # 将图片保存为PNG格式

def get_html(url):  # 定义一个函数，用于获取网页的HTML源代码
    driver.get(url)  # 访问指定的URL
    time.sleep(random.random())  # 等待0.3秒，让网页加载完成
    for i in range(1500):  # 循环1500次
        driver.execute_script('window.scrollBy(0, 15)')  # 执行JavaScript代码，使浏览器滚动
    time.sleep(random.random())  # 等待0.5秒，让网页加载完成
    html = driver.page_source  # 获取网页的HTML源代码
    return html  # 返回HTML源代码

def scrap_images(url, folder):  # 定义一个函数，用于从指定的URL抓取图片
    global image_counter  # 声明全局变量image_counter
    html = get_html(url)  # 获取网页的HTML源代码
    soup = BeautifulSoup(html, 'html.parser')  # 用BeautifulSoup解析继续给上面代码的注释：
    print("?1")
    # HTML源代码
    groups = soup.find_all('div', class_='wp-block-template-part')  # 找到所有的class为'wp-block-template-part'的div标签
    #print(groups)
    for group in groups:  # 遍历每个div
        image = group.find('img')  # 在div中找到img标签
        src = image.get('src')  # 获取img的src属性，即图片的URL
        title = group.find('h2').text.strip()  # 在div中找到h2标签，并获取其文本内容作为图片的标题
        subfolder = os.path.join(folder, title)  # 构造子文件夹的路径
        if not os.path.exists(subfolder):  # 如果子文件夹不存在
            os.makedirs(subfolder)  # 创建子文件夹
        image_counter=1  # 初始化图片计数器
        print("?2")
        save_imgs(title, src, subfolder,image_counter)  # 调用save_imgs函数，下载并保存图片
        print("?3")
        image_counter+=1  # 图片计数器加1
        a_tag = group.find('a')  # 在div中找到a标签
        if a_tag is not None and 'href' in a_tag.attrs:  # 如果a标签存在，并且有href属性
            print("?3")
            link = a_tag['href']  # 获取a标签的href属性，即链接的URL
            print("?4")
        html_first = get_html(link)  # 访问链接，获取网页的HTML源代码
        print("?5")
        soup_first = BeautifulSoup(html_first, 'html.parser')  # 用BeautifulSoup解析HTML源代码
        ul_tag = soup_first.find('ul', class_='page-links')  # 在HTML中找到class为'page-links'的ul标签
        if ul_tag is not None:  # 如果ul标签存在
            li_tags = ul_tag.find_all('li')  # 在ul中找到所有的li标签
            num_of_li = len(li_tags)  # 获取li标签的数量
        else:  # 如果ul标签不存在
            num_of_li = 1  # li标签的数量设为1
        for i in range(1, num_of_li + 1):  # 遍历每个li标签
            link_detail = link + f"/{i}"  # 构造详细页面的URL
            html_detail = get_html(link_detail)  # 访问详细页面，获取网页的HTML源代码
            soup_detail = BeautifulSoup(html_detail, 'html.parser')  # 用BeautifulSoup解析HTML源代码
            groups_detail = soup_detail.find_all('figure', class_='wp-block-image size-large')  # 在HTML中找到所有的class为'wp-block-image size-large'的figure标签
            for group_detail in groups_detail:  # 遍历每个figure标签
                image_detail = group_detail.find('img')  # 在figure中找到img标签
                src_detail = image_detail.get('src')  # 获取img的src属性，即图片的URL
                save_imgs(title, src_detail, subfolder,image_counter)  # 调用save_imgs函数，下载并保存图片
                image_counter+=1  # 图片计数器加1
    time.sleep(random.random())  # 等待0.5秒，继续给上面代码的注释：


    # 以免过于频繁的请求导致被网站封禁
    print("OK")  # 打印消息，表示该网页的图片已经全部抓取完成

folder = 'D:\\PaQv\\PaQv4khdB'  # 设置图片保存的目录
if not os.path.exists(folder):  # 如果目录不存在
    os.makedirs(folder)  # 创建目录
base_url= "https://www.4khd.com/?query-3-page={}&cst"  # 设置网站的基础URL，其中{}会被替换为具体的页码
for page in range(3, 255):  # 遍历从...到254的每个页码
    scrap_images(base_url.format(page), folder)  # 调用scrap_images函数，抓取并保存该页的所有图片
time.sleep(12)  # 等待12秒，以免过于频繁的请求导致被网站封禁
