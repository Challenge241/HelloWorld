# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 10:58:38 2023

@author: Lenovo
"""

from selenium import webdriver
import time

# 创建driver对象
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# 访问网址
driver.get('https://www.jd.com')

driver.find_element(By.CSS_SELECTOR, '#key').send_keys('手机')
driver.find_element(By.CSS_SELECTOR, '#search > div > div.form > button').click()
time.sleep(2)


# 向下滑动   # 可以执行js代码的方法
for i in range(1000):
    driver.execute_script('window.scrollBy(0, 5)')

# 等待这个浏览器充分加载完毕之后
# 获取网页源代码
"""   包含静态和动态数据   """
html = driver.page_source
print( html )
time.sleep(100)