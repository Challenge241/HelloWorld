# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 10:03:23 2023

@author: Lenovo
"""

"""
大图
https://tppic.chinaz.net/files/default/imgs/2023-06-14/7bb386296ae257e1_big.jpg
小图
https://tppic.chinaz.net/files/default/imgs/2023-06-09/571c081dc00d226d_big.jpg


1、通过首页获取首页的所有图片链接
2、跳转到所有图片的链接地址
3、通过图片的链接地址，获取里面的大图链接
"""
# 导入requests库，用于网络请求
# 导入BeautifulSoup库，用于解析HTML
import requests
from bs4 import BeautifulSoup

# 设置爬虫的基础URL
url = "https://sc.chinaz.com/tupian/"

# 开始循环，范围从1到10（包括1和10），爬取前10页的图片
for i in range(1,11):

    # 如果i大于1，说明不是第一页，需要在URL后面加上'index_{}.html'的后缀，形如'index_2.html'，表示第二页
    if i > 1 :
        url = url + 'index_{}.html'.format(i)
    else:
        # 如果i等于1，说明是第一页，不需要改变URL，跳过
        pass

    # 设置请求头，模拟浏览器访问
    hd = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.39'
    }

    # 使用requests库的get方法访问URL，并设置请求头，返回Response对象
    res = requests.get(url, headers=hd)

    # 将Response对象的编码设置为'utf-8'，以正常解析中文字符
    res.encoding = 'utf-8'

    # 使用BeautifulSoup库解析HTML文本，得到一个BeautifulSoup对象
    soup = BeautifulSoup(res.text, 'html.parser')

    # 在BeautifulSoup对象中找到包含图片的div元素
    div = soup.find('div', attrs={'class':'tupian-list'})

    # 在这个div元素中找到所有的img元素，返回一个列表
    img_all = div.find_all('img')

    # 遍历img元素的列表
    for img in img_all:

        # 处理图片的URL，获取大图的URL
        img_url = 'https://tppic.' +  '.'.join(img['data-original'].split('.')[1:]).replace('_s', '_big')

        # 获取图片的名字，用于保存到本地
        img_name = img['alt']

        # 使用requests库的get方法下载图片
        img_res = requests.get(img_url, headers=hd)

        # 打开一个新的文件，文件名为图片的名字，模式为'wb'，即写入二进制数据
        with open(f'{img_name}.jpg', 'wb') as f:

            # 将下载的图片内容写入文件
            f.write(img_res.content)

        # 打印100个'='，表示已经完成这张图片的下载
        print('='*100)
