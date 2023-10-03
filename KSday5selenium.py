# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 10:57:24 2023

@author: Lenovo
"""

"""
selenium
    第三方模块
        pip install selenium
    Selenium是一个用于Web应用程序测试的工具。
    Selenium测试直接运行在浏览器中，就像真正的用户在操作一样
    
    代码  ->    驱动   ->    浏览器
    
    chrome : 浏览器的版本:  112.0.5615.50
    edge: 112.0.1722.39 
    
"""
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


# 创建driver对象
driver = webdriver.Chrome()

# driver = webdriver.Edge()
# webdriver.Firefox()
# 设置浏览器的窗口最大化
driver.maximize_window()
# 访问网址
driver.get( 'https://www.baidu.com' )

# 1、定位标签
kw = driver.find_element(By.CSS_SELECTOR,  '#kw'   )
# 如果定位成功，那么就会返回一个对象
# 2、输入内容
kw.send_keys('千锋')
#3、定位百度一下按钮
su = driver.find_element(By.CSS_SELECTOR, '#su')
# 4、点击这个按钮
su.click()
time.sleep(2)
# 截图  截取当前所展示的整个窗口内容
driver.save_screenshot('百度一下.png')

# 定位搜索结果数量
search = driver.find_element(By.CSS_SELECTOR, '#tsn_inner > div:nth-child(2)')
search.screenshot('搜索结果数量.png')





time.sleep(10)