# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 10:06:26 2023

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
# # 登录，获取用户的身份令牌
login_url = "https://passport.17k.com/ck/user/login"
# # 请求头信息
hd = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.39'
}
# 请求的参数
data = {
    'loginName': '13168837959',
    'password': 'a343105980'
}
login_res = requests.post( login_url, headers=hd, data=data)
# 登录的作用就是 获取token
# token 是在请求之后的  返回头部信息中
set_cookie = login_res.headers['Set-Cookie'].split(';')
cookie = ''
for i in set_cookie:
    if 'accessToken' in i:
        cookie = i.split(',')[-1].lstrip()
print( cookie )
# 书架访问方式
url = "https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919"
hd['cookie'] = 'accessToken=avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F19%252F19%252F78%252F77537819.jpg-88x88%253Fv%253D1622982584000%26id%3D77537819%26nickname%3D%25E8%2583%2596%25E5%25A2%25A9%25E5%25A2%25A9%25E6%2595%25A6%25E6%2595%25A6%25E6%2595%25A6%25E6%2595%25A6%26e%3D1702259055%26s%3D30f953a6e5f540c0'
res = requests.get( url , headers=hd)
print( res.text  )

