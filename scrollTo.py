# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 23:05:35 2023

@author: Lenovo
"""

from selenium import webdriver
import time

# 创建一个Chrome浏览器实例
driver = webdriver.Chrome()
# 打开指定的网页
driver.get('http://www.xinfadi.com.cn/priceDetail.html')
'''
# 通过模拟滚动操作，不断地滚动网页
while True:
    # 在滚动操作前，记录滚动高度
    last_height = driver.execute_script("return document.body.scrollHeight")

    # 滚动到页面的底部
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # 等待页面加载
    time.sleep(2)

    # 计算新的滚动高度，然后与上一次的滚动高度进行比较
    new_height = driver.execute_script("return document.body.scrollHeight")

    # 当滚动操作后，滚动高度无法更新（已经到达底部）时，跳出循环
    if new_height == last_height:
        break
'''
while True:
    # 在滚动操作前，记录滚动条的高度
    last_height = driver.execute_script("return document.body.scrollHeight")
    print(last_height)
    # 滚动一段距离
    driver.execute_script('window.scrollBy(0, 100)')

    # 等待页面加载
    time.sleep(0.1)  # 调整为合适的等待时间

    # 计算新的滚动条的高度，然后与上一次的滚动高度进行比较
    new_height = driver.execute_script("return document.body.scrollHeight")
    print(new_height)
    # 当滚动操作后，滚动条的高度无法更新（已经到达底部）时，跳出循环
    if new_height == last_height:
        break
