# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 10:24:43 2023

@author: Lenovo
"""
#该网站有一些反爬机制，这导致我没能成功爬取其
import requests
import json
import time
url = 'https://scrapingclub.com/exercise/ajaxdetail_header/'  # 替换为实际的Ajax请求URL
#设置合适的User-Agent
headers = {
    'Referer': 'https://www.example.com',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36 Edg/114.0.1823.51'
}
'''
print('requests.cookies:'+str(requests.cookies))
cookies = requests.cookies.RequestsCookieJar()
cookies.set('cookie_name', 'cookie_value')
Referer='https://scrapingclub.com/exercise/detail_header/'
'''
response = requests.get(url, headers=headers)
'''
#处理Cookies
session = requests.Session()
session.get(url)  # 这将获取和处理Cookies
response = session.get(url)  # 使用相同的会话发送请求
#处理重定向
response = requests.get(url,headers=headers,Cookie=Cookie)  # 禁止自动重定向
if response.status_code == 302:  # 处理特定的重定向状态码
    redirect_url = response.headers['Location']
    response = requests.get(redirect_url)
    '''
#添加延迟
time.sleep(0.5)
#检查
print("response.status_code:"+str(response.status_code))
print("response.headers:"+str(response.headers))
print("response.content:"+str(response.content))
print("response.text:"+response.text)

'''
data = response.json()

# 提取产品详细信息
title = data['title']  # 替换为实际的标题键路径
description = data['description']  # 替换为实际的描述键路径
price = data['price']  # 替换为实际的价格键路径

# 打印产品详细信息
print('Title:', title)
print('Description:', description)
print('Price:', price)
'''



