# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 10:04:49 2023

@author: Lenovo
"""

import requests
import csv


file = open('北京新发地.csv', 'w', encoding='utf-8-sig', newline='')
csv_file = csv.writer( file )
csv_file.writerow(['菜名','发布时间'])

url = "http://www.xinfadi.com.cn/getPriceData.html"
hd = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.39'
}
data = {
    'limit': '',
    'current': '',
    'pubDateStartTime': '',
    'pubDateEndTime': '',
    'prodPcatid': '',
    'prodCatid': '',
    'prodName': ''
}

for i in range(1,11):
    if i == 1:
        pass
    else:
        data['limit'] = 20
        data['current'] = i
    res = requests.post( url, headers=hd, data=data)
    data = res.json()
    data_list = data['list']
    for i in data_list:
        name = i['prodName']
        pubdate = i['pubDate']
        csv_file.writerow([ pubdate, name])