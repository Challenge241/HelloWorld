# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 11:44:17 2023

@author: Lenovo
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# 创建 WebDriver 实例（这里使用 Chrome 浏览器）
driver = webdriver.Chrome()

# 打开第一个页面
driver.get("https://www.baidu.com")
time.sleep(1)
# 在新窗口中打开第二个页面
driver.execute_script("window.open('https://www.google.com', '_blank');")
time.sleep(1)
# 获取当前窗口的句柄（用于切换回第一个页面）
first_window = driver.current_window_handle
time.sleep(1)
# 获取所有窗口的句柄
all_windows = driver.window_handles

# 切换到新打开的窗口
for window in all_windows:
    if window != first_window:
        driver.switch_to.window(window)

# 在新窗口中执行一些操作
print("Current URL:", driver.current_url)

# 切换回第一个页面
driver.switch_to.window(first_window)
time.sleep(1)
# 在第一个页面中执行一些操作
print("Current URL:", driver.current_url)

# 关闭浏览器
#driver.quit()
