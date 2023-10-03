# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 11:52:56 2023

@author: Lenovo
"""

import requests             # 导入 requests 库，用于网络请求
from bs4 import BeautifulSoup   # 导入 BeautifulSoup 库，用于网页解析
import json                # 导入 json 库，用于处理 json 数据
import csv                 # 导入 csv 库，用于处理 csv 文件

def get_hotel_info(hotelid):   # 定义函数，参数为酒店的 id
    # 酒店详情页面的 URL，使用 format 方法，将酒店 id 填充到 URL 中
    url = "https://hotels.ctrip.com/hotels/detail/?hotelId={}&cityId=2".format(hotelid) 
    res = requests.get(url)   # 使用 requests 库的 get 方法，对酒店详情页面进行网络请求，返回结果赋值给 res
    soup = BeautifulSoup(res.text, 'html.parser')  # 使用 BeautifulSoup 库解析网页内容，解析器选择 'html.parser'
    script_all = soup.find_all('script')  # 使用 BeautifulSoup 的 find_all 方法，找出所有的 script 标签，返回结果赋值给 script_all
    for script in script_all:  # 遍历所有的 script 标签
        content = script.text  # 获取 script 标签的文本内容
        # 判断文本内容中是否含有 'window.IBU_HOTEL'
        if 'window.IBU_HOTEL' in content:  
            content = ';'.join(content.split(';')[1:4]).strip()  # 切割字符串，并用 ';' 连接选定的部分，然后去除两端的空白
            content = content[content.index('=') + 1:]  # 找到'='的位置，并截取其后的字符串
            # 把json数据转化成 字典
            data = json.loads(content)  # 使用 json 库的 loads 方法，将字符串形式的 json 数据转换为 Python 的字典
            # 通过字典的键值对获取信息
            basic = data['initData']['staticHotelInfo']['hotelInfo']['basic']  
            print(basic['label'][-1].split('：')[-1])  # 打印最后一个 'label' 的值，这可能是一些酒店信息
            print(basic['description'])  # 打印 'description' 的值，这可能是酒店描述
            print(basic['name'])  # 打印 'name' 的值，这可能是酒店名字
        print('=' * 200)  # 打印分割线
get_hotel_info()  # 调用函数，应输入需要查询的酒店 id
