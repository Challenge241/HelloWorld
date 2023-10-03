# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 10:30:42 2023

@author: Lenovo
"""

'''
所有分类所有页面的文章
单个分类的所有页面文章
单个分类的单个页面文章
单个页面单个文章

分析页面：
    静态
'''
""""""
"""
1、目的就爬取励志一生的所有文章
    所有分类中的所有页面的文章   获取所有的文章分类
    单个分类的所有页面文章  √
    单个页面所有文章   √
    单个页面单个文章   √
2、分析页面
    静态

"""
import requests  # 导入请求库，用于发出HTTP请求
from bs4 import BeautifulSoup  # 导入BeautifulSoup库，用于解析HTML
import os  # 导入os库，用于文件和目录操作

# 创建一个类，封装爬虫功能
class lizhiYsheng():
    def __init__(self):
        # 初始化各个链接和请求头
        self.home_link = "https://www.lz13.cn/"  # 首页链接
        self.class_link = "https://www.lz13.cn/lizhi/lizhichuangye.html"  # 分类链接
        self.article_link = "https://www.lz13.cn/lizhiwenzhang/184124.html"  # 文章链接
        # 请求头，伪装浏览器访问
        self.hd = {
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.39'
        }

    # 请求方法，返回解析后的HTML文档
    def requests_get(self, url, hd):
        res = requests.get( url, headers=hd)  # 发送请求
        res.encoding = 'utf-8'  # 设置编码
        soup = BeautifulSoup(res.text, 'html.parser')  # 解析HTML
        return soup  # 返回解析后的文档

    # 文章的解析方法，返回文章内容和标题
    def article_parser(self, soup):
        div = soup.find('div', attrs={'class':'PostContent'})  # 定位到文章内容的div
        p_all = div.find_all('p')  # 获取所有段落
        title = soup.title.string  # 获取文章标题
        content = ''  # 初始化内容字符串
        for p in p_all:  # 遍历所有段落
            content += p.text.strip() + '\n'  # 去除空格并换行
        return content, title  # 返回内容和标题

    # 保存文件的方法，将内容保存到指定的文件
    def save_content(self, content, filename):
        with open(filename, 'w', encoding='utf-8') as f:  # 打开文件
            f.write( content )  # 写入内容

    # 分类的解析方法，返回文章链接列表
    def class_parser(self, soup ):
        article_link_list = []  # 初始化链接列表
        div_all = soup.find_all('div', attrs={'class':'PostHead'})  # 定位到文章的div
        for div in div_all:  # 遍历所有div
            article_link = div.h3.a['href']  # 获取文章链接
            article_link_list.append( article_link)  # 添加到链接列表
        return article_link_list  # 返回链接列表
    #获取分页的页码数量
    def get_page_num(self , soup):
        pager = soup.find('div', attrs={'class':'pager'})  # 定位到分
        num = pager.find_all('a')[1]['href'].split('-')[-1].split('.')[0] # 获取分页的页码数量
        return num # 返回页码数量

    # 处理文章的公共方法
def chuli_article(self , article_link_list, class_title):
    for article_link in article_link_list:  # 遍历文章链接列表
        soup = self.requests_get(article_link, self.hd)  # 获取并解析文章页面
        content, title = self.article_parser(soup)  # 解析文章，获取内容和标题
        self.save_content(content, f'{class_title}/{title}.txt')  # 保存内容到文件
        print( '文章：{},{}  保存成功'.format(class_title, title ))  # 打印保存成功的消息

# 创建目录的方法
def create_dir(self, path):
    if not os.path.exists( path ):  # 如果路径不存在
        os.mkdir( path )  # 创建目录

#  解析首页源码，获取各个分类
def home_parser(self, home_soup):
    class_content = []  # 初始化分类列表
    div = home_soup.find('div', attrs={'id':'MainMenu'})  # 定位到菜单的div
    a_all = div.find_all('a')  # 获取所有链接
    for a in a_all:  # 遍历所有链接
        class_link = a['href']  # 获取分类链接
        class_title = a.string  # 获取分类标题
        self.create_dir( class_title )  # 创建对应的目录
        class_content.append( [class_link, class_title]  )  # 添加到分类列表
    return class_content  # 返回分类列表

# 启动方法
def run(self):
    # 请求并解析首页
    home_soup = self.requests_get(self.home_link, self.hd)
    # 解析首页源码，获取各个分类  [分类链接, 分类标题]
    class_content = self.home_parser( home_soup )
    # 遍历分类
    for class_link, class_title in class_content:
        # 请求并解析分类页面
        class_soup_one = self.requests_get( class_link, self.hd )
        # 获取文章链接列表
        article_link_list = self.class_parser( class_soup_one )
        # 处理并保存文章
        self.chuli_article(  article_link_list , class_title)
        # 获取分页的页码数量
        page_num = self.get_page_num( class_soup_one )
        print( '当前分类的页码是剩余{}页'.format(page_num))  # 打印页码数量
        url = '.'.join( self.class_link.split('.')[:-1] )  # 构造分类页面的基础链接
        # 遍历所有分页
        for i in range(1, int(page_num)+1 )[::-1] :
            class_link = url+ '-' + str(i) + '.html'  # 构造分页链接
            # 请求并解析分页
            class_soup = self.requests_get(class_link, self.hd)
            # 获取文章链接列表
            article_link_list = self.class_parser( class_soup )
            # 处理并保存文章
            self.chuli_article( article_link_list, class_title )



if __name__ == '__main__':
    lz = lizhiYsheng()
    lz.run()