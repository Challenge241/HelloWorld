# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 09:10:00 2023

@author: Lenovo
"""

'''
爬虫四类:
    通用网络爬虫
    聚焦网络爬虫
    增量网络爬虫（爬取网站新更新的数据的爬虫）
    深度网络爬虫（需要提供表单信息，例如账号密码）

爬取的数据分类：
    用户产生的
    政府产生的
    公司管理的
    自己爬取的

页面数据分类：
    静态数据： 用搜网页源码的功能，可以看到网页源码含有那些数据
    动态数据：通过一定的触发条件而再次加载的数据，动态数据，捕获接口，进行请求访问，例如百度搜出来的图片，
    这些数据用网页源码的搜索功能搜不出

浏览器调试
    元素
        包含静态数据与动态数据
        分析页面数据类型
        
        请求方法POST有参数，Get没有参数
        状态码200代表请求成功
        
        User-Agent浏览器的属性信息，用其，会使网站觉得是浏览器在访问其
        Cookie：轻量级的保存数据的，主要是保存用户登录信息的
聚合数据网站是第三方数据公司

robots协议
    网站不允许爬虫去访问某些子站点
    网站禁止爬虫访问某些子站点
    
反爬机制：
    验证码，点击，点选，滑块，登录验证
    js加密
    文字混淆，字体库
    ip封禁,一分钟内访问次数过多，ip就会被封禁
    手机端 app加密算法
    读取用户运行轨迹
    防盗链
    
解密需要汇编、java与前端知识，老师破解抖音花了7个月，然后过了1个月，抖音升级，用了新的加密算法，原来的解密爬取数据的方法失效了
解密需要java、安卓、前端、机器学习、深度学习、汇编

url的组成部分：
    网络协议、域名、参数
    网络协议http在一般情况是没有什么反爬措施
    网络协议https是很可能有反爬措施的，https中的s代表的是ssl，ssl是一种安全协议
    www.baidu.com域名
    /s
    ?wd=python  意为搜索python
    #代表锚点  百度百科当前页面第五章的锚点是5，锚点用于在当前页面进行跳转
    把一部分删掉看是否变了，来判断那一部分是否有用
    
get可用于下载
post可用于上传

网络上的接口数据一般情况下都是json数据
把json字符串数据转换为字典数据
'''

'''
# 导入requests库用于发起HTTP请求，导入json库用于处理JSON格式的数据
import requests
import json

# 定义一个函数，用GET方式向http://httpbin.org/get发起请求
def get_request():
    # 使用requests库的get函数发送GET请求
    response = requests.get('http://httpbin.org/get')
    # 打印提示信息
    print("GET Request:")
    # 打印服务器返回的响应，使用json库的dumps函数将返回的JSON数据转化为字符串，indent参数设置缩进量，以便于阅读
    print(json.dumps(response.json(), indent=4))

# 定义一个函数，用POST方式向http://httpbin.org/post发起请求
def post_request():
    # 使用requests库的post函数发送POST请求，data参数用于指定需要发送的数据
    response = requests.post('http://httpbin.org/post', data = {'key':'value'})
    # 打印提示信息
    print("\nPOST Request:")
    # 打印服务器返回的响应，使用json库的dumps函数将返回的JSON数据转化为字符串，indent参数设置缩进量，以便于阅读
    print(json.dumps(response.json(), indent=4))

# 定义一个函数，用PUT方式向http://httpbin.org/put发起请求
def put_request():
    # 使用requests库的put函数发送PUT请求，data参数用于指定需要发送的数据
    response = requests.put('http://httpbin.org/put', data = {'key':'value'})
    # 打印提示信息
    print("\nPUT Request:")
    # 打印服务器返回的响应，使用json库的dumps函数将返回的JSON数据转化为字符串，indent参数设置缩进量，以便于阅读
    print(json.dumps(response.json(), indent=4))

# 定义主函数，该函数会依次调用get_request, post_request, put_request这三个函数
def main():
    get_request()
    post_request()
    put_request()

# 如果这个Python文件是被直接运行，而不是被其他文件导入，那么就运行main函数
if __name__ == "__main__":
    main()
'''

'''
# 导入所需的库
import requests           # 用于发送HTTP请求
from bs4 import BeautifulSoup  # 用于解析HTML
import pandas as pd       # 用于数据处理和分析

# 定义一个函数，用于爬取给定URL的图书信息
def scrape_books(url):
    response = requests.get(url)  # 发送GET请求
    soup = BeautifulSoup(response.text, 'html.parser')  # 将返回的HTML内容解析为BeautifulSoup对象

    # 找到所有的图书元素，这些元素的HTML标签是'article'，CSS类名是'product_pod'
    books = soup.find_all('article', class_='product_pod')
    data = []  # 用于存储所有图书的信息

    # 对每本图书进行处理
    for book in books:
        # 找到图书的名字，名字在一个'h3'标签下的'a'标签的'title'属性中
        name = book.find('h3').find('a')['title']
        # 找到图书的价格，价格在一个'p'标签下，这个'p'标签的CSS类名是'price_color'
        price = book.find('p', class_='price_color').text
        # 将图书的名字和价格添加到data列表中
        data.append([name, price])

    # 返回所有图书的信息
    return data

# 定义main函数，这是程序的主入口
def main():
    url = 'http://books.toscrape.com/'  # 要爬取的URL
    data = scrape_books(url)  # 爬取图书信息

    # 将图书信息转换为DataFrame，并设置列名为'Book Title'和'Price'
    df = pd.DataFrame(data, columns=['Book Title', 'Price'])
    # 将DataFrame保存为CSV文件，文件名为'books.csv'，不保存行索引
    df.to_csv('books.csv', index=False)
    print("Scraping done. Data saved to 'books.csv'.")  # 打印成功信息

# 如果这个文件是被直接运行的，而不是被导入的，那么就运行main函数
if __name__ == "__main__":
    main()
'''
import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin

def scrape_books(base_url):
    data = []
    url = base_url
    while url:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        books = soup.find_all('article', class_='product_pod')
        for book in books:
            name = book.find('h3').find('a')['title']
            price = book.find('p', class_='price_color').text
            data.append([name, price])

        # 寻找下一页的链接，如果存在则更新url，不存在则结束循环
        next_link = soup.find('li', class_='next')
        if next_link:
            relative_url = next_link.find('a')['href']
            url = urljoin(base_url, relative_url)  # 这里修改为基于当前url进行拼接
        else:
            url = None
        base_url='http://books.toscrape.com/catalogue/'
    return data

def main():
    base_url = 'http://books.toscrape.com'  # 修改为包含"catalogue/"的URL
    data = scrape_books(base_url)

    df = pd.DataFrame(data, columns=['Book Title', 'Price'])
    df.to_csv('books.csv', index=False)
    print("Scraping done. Data saved to 'books.csv'.")

if __name__ == "__main__":
    main()
'''
import pandas as pd

# 读取csv文件
df = pd.read_csv('books.csv')

# 计算平均值
mean_value = df["Price"].mean()
print(f'Mean: {mean_value}')

# 计算中位数
median_value = df["Price"].median()
print(f'Median: {median_value}')

'''