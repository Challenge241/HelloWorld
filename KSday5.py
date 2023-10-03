# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 09:08:49 2023

@author: Lenovo
"""

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.maximize_window()
time.sleep(0.5)


#定位标签
kw=driver.find_element(By.CSS_SELECTOR,'#kw')
#输入内容
kw.send_keys('千峰')
#定位百度一下
su=driver.find_element(By.CSS_SELECTOR,'#su')

#点击
su.click()

#截图
#driver.save_screenshot('百度一下.png')
'''
#?
#定位搜索结果数量
driver.find_element(By.CSS_SELECTOR,'#tsn_inner > div:nth-child(1) > span.close_wrapper_2yHC1 > span').click()
time.sleep(1)
#tsn_inner > div:nth-child(1) > span.close_wrapper_2yHC1 > span
search=driver.find_element(By.CSS_SELECTOR,'#tsn_inner > div:nth-child(2) > span')
#print(search)
driver.save_screenshot('搜索结果数量.png')
'''
for i in range(100):
    driver.execute_script('window.scrollBy(0,10)')
    time.sleep(0.05)
    
#等待浏览器充分加载完毕之后获取网页源码
"""包含动态与静态数据"""
driver.get('http://www.xinfadi.com.cn/index.html')
html=driver.page_source
print(html)
from bs4 import BeautifulSoup
soup=BeautifulSoup(html,'html.parser')

time.sleep(5)
