# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 09:46:45 2023

@author: Lenovo
"""

"""
访问书架的内容
    1、登录
    2、获取token信息
    3、发送书架的请求连接，必须要携带token
    4、才可以获取书架的内容
    


书架的访问链接
    https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919
    
登录接口
    https://passport.17k.com/ck/user/login
"""

import requests


# 登录的URL地址
login_url = "https://passport.17k.com/ck/user/login"

# 定义请求头信息，包括用户代理信息等，用于伪装浏览器访问
hd = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.39'
}

# 定义请求的参数，包括登录名和密码
data = {
    'loginName': '13168837959',
    'password': 'a343105980'
}

# 使用requests库的post方法进行登录操作，将请求头信息和数据参数一起发送给服务器
login_res = requests.post( login_url, headers=hd, data=data)

# 服务器响应中的Set-Cookie字段中含有我们需要的token信息
# 通过split(';')操作，将这个字段中的信息分割成单独的cookie
set_cookie = login_res.headers['Set-Cookie'].split(';')
cookie = ''

# 遍历这些cookie，查找含有"accessToken"的那一项，这就是我们需要的token
for i in set_cookie:
    if 'accessToken' in i:
        cookie = i.split(',')[-1].lstrip()

print( cookie )

# 定义书架的URL地址
url = "https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919"

# 将获取到的token添加到请求头信息中，作为cookie字段的值
hd['cookie'] = 'accessToken=avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F19%252F19%252F78%252F77537819.jpg-88x88%253Fv%253D1622982584000%26id%3D77537819%26nickname%3D%25E8%2583%2596%25E5%25A2%25A9%25E5%25A2%25A9%25E6%2595%25A6%25E6%2595%25A6%25E6%2595%25A6%25E6%2595%25A6%26e%3D1702259055%26s%3D30f953a6e5f540c0'

# 使用requests库的get方法进行访问，发送带有token的请求头信息给服务器
res = requests.get( url , headers=hd)

# 打印服务器返回的数据
print(res.text)
