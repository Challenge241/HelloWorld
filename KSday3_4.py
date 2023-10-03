# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 10:11:30 2023

@author: Lenovo
"""

import requests
import csv


file = open('京东评论.csv', 'w', encoding='utf-8-sig', newline='')
csv_file = csv.writer( file)
csv_file.writerow( ['评分','创建时间','评论内容'] )



for page in range(0, 11):
    url = "https://api.m.jd.com/?appid=item-v3&functionId=pc_club_productPageComments&client=pc&clientVersion=1.0.0&t=1686711440582&loginType=3&productId=100050641649&score=0&sortType=5&page={}&pageSize=10".format(page)
    hd = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.39'
    }
    res = requests.get( url, headers=hd)
    comments_list = res.json()['comments']
    for comment in comments_list:
        content = comment['content'].replace('\n','')
        creationTime = comment['creationTime']
        score = comment['score']
        print( '分数：{}， 创建时间：{}， 内容：{}'.format(score, creationTime, content))
        csv_file.writerow([ score, creationTime, content ] )