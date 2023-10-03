# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 11:18:16 2023

@author: Lenovo
"""
COOKIES='_gid=GA1.2.1284048203.1686968051; csrftoken=X3l19t1HdB7hwo83QdFWhdKOvkYPiJLdfYh9EZKQkh8BkvCj3fBS07GlHedUu1NB; _gat_gtag_UA_39890589_8=1; _ga=GA1.1.1772160099.1686627215; _ga_X40J0LF5BP=GS1.1.1686968050.5.1.1686970359.0.0.0'
set_cookie = COOKIES.split(';')
print(set_cookie)
cookie = ''
# 遍历这些cookie，查找含有"accessToken"的那一项，这就是我们需要的token
for i in set_cookie:
    if 'accessToken' in i:
        cookie = i.split(',')[-1].lstrip()

print( cookie )