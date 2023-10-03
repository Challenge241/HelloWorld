# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 15:58:03 2023

@author: Lenovo
"""

import requests
import csv

url = 'https://jiameng.baidu.com/portal/search/indexV2?ajax=1&accessid=0388707990D6&device=wise&from=jmx&category=20600&pageSize=10&page=1&repeatKey=0'  

response = requests.get(url)

# 检查状态码
if response.status_code == 200:
    # 如果返回的是JSON数据，可以直接使用.json()方法将其解析为Python字典
    content = response.json()
    data=content['data']
    # 创建CSV文件并写入数据
    with open('output.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ProductName", "CompanyName", "PriceInfo"])  # 写入表头

        
        for list in data.get('list', []):
            product_name = list.get('productName')  
            company_name = list.get('companyName')  
            price_info = list.get('priceInfo')  

            writer.writerow([product_name, company_name, price_info])  # 写入一行数据

else:
    print('Failed to retrieve data: status code', response.status_code)
