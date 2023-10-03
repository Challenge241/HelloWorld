# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 11:53:42 2023

@author: Lenovo
"""

loginname = ''   # 用户登录名，需要填入具体值
passwd = ''      # 用户密码，需要填入具体值

# 导入所需的库和模块
from selenium import webdriver  # 用于模拟浏览器操作
import requests  # 用于发送网络请求
from bs4 import BeautifulSoup  # 用于解析网页
import time  # 用于程序中的时间操作，如延时等待
from selenium.webdriver.common.by import By  # 用于定位网页元素
import json  # 用于处理json数据
import csv  # 用于处理csv文件

# 定义变量
hid = 11  # 酒店id
cityid = 1  # 城市id

# 打开文件，并创建csv.writer对象，准备写入数据
file = open('酒店详情.csv', 'w', encoding='utf-8-sig', newline='')
csv_file = csv.writer(file)
csv_file.writerow(['酒店电话', '酒店详情', '酒店名称'])  # 写入表头

# 定义函数，用于获取酒店信息
def get_hotel_info(hotelid):
    # 酒店详情页面的 URL，使用 format 方法，将酒店 id 填充到 URL 中
    url = "https://hotels.ctrip.com/hotels/detail/?hotelId={}&cityId=2".format(hotelid) 
    res = requests.get(url)  # 使用 requests 库的 get 方法，对酒店详情页面进行网络请求，返回结果赋值给 res
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
            tel = basic['label'][-1].split('：')[-1]  # 获取并解析电话信息
            des = basic.get('description')  # 获取酒店描述
            name = basic.get('name')  # 获取酒店名称
            csv_file.writerow([tel, des, name])  # 将获取的信息写入 csv 文件
            print([tel, name, des])  # 在控制台打印信息
        print('=' * 200)  # 打印分隔线
        
# 初始化浏览器驱动，开始模拟浏览器操作
driver = webdriver.Chrome()
driver.get('https://hotels.ctrip.com/hotels/list?countryId=1&city=2&directSearch=0&display=%E4%B8%8A%E6%B5%B7')  # 访问携程酒店列表页面
time.sleep(5)  # 等待5秒，等待页面加载
# 输入登录信息并登录
nloginname = driver.find_element(By.ID, 'nloginname')  # 找到用户名输入框
nloginname.send_keys(loginname)  # 输入用户名
time.sleep(0.8)
npwd = driver.find_element(By.ID, 'npwd')  # 找到密码输入框
npwd.send_keys(passwd)  # 输入密码
time.sleep(0.7)
# 点击协议
ca = driver.find_element(By.ID, 'checkboxAgreementInput')
ca.send_keys(' ')
time.sleep(0.5)
# 点击登录
driver.find_element(By.ID, 'nsubmit').click()
time.sleep(3)
# 登录后重新访问其他页面
driver.get('https://m.ctrip.com/webapp/hotels/list?city=2&atime=20230616&days=1')
time.sleep(1)
# 暂时未使用的向下滑动操作，可以执行js代码的方法
# for i in range(300):
#     driver.execute_script('window.scrollBy(0, 10)')
#     time.sleep(0.05)
time.sleep(5)
# 获取源码
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')  # 解析页面源码
hotel_item = soup.find_all('div', attrs={'class':'hotel-item'})  # 找到所有酒店元素
for hotel in hotel_item:  # 遍历所有酒店元素
    hotelid = hotel.a.div['hotelid']  # 获取酒店id
    get_hotel_info(hotelid)  # 获取并处理酒店信息
    print('='*100)  # 打印分隔线
