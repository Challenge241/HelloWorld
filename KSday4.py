# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 09:13:06 2023

@author: Lenovo
"""

#html.parser解释器
#soup=BeautifulSoup(url,解释器)
#soup.title返回找到的第一个title,否则返回空
#soup.find可以进行属性的过滤
#soup.find(标签名称，attrs={'属性名称':'属性值'})
#soup.find_all(标签名称，attrs={'属性名称':'属性值'})返回一个序列
'''在标签中提取属性：
meta[content]
'''

'''
方法一：
1、通过首页
2、进入小图
3、抵达大图
方法二：
1、通过首页找到小图链接
2、然后修改小图链接，改成大图链接
3、下载大图
'''

'''
懒加载：只加载用户看得到的地方，从而提升加载速度，提高用户体验
避免懒加载有两种方式：

'''
'''
import requests
from bs4 import BeautifulSoup
url='https://sc.chinaz.com/tupian/'
res=requests.get(url)
res.encoding='utf-8'
soup= BeautifulSoup(url,'html.parser')
'''

'''
for img in img_all:
    print((img['data-original'].split('.')[1:]).replace())
    print('='*100)
'''    


def transform_url(old_url):
    # 将url替换为新的url
    new_url = old_url.replace("scpic1.chinaz.net", "tppic.chinaz.net")
    # 将文件名末尾的 _s.jpg 替换为 _big.jpg
    new_url = new_url.replace("_s.jpg", "_big.jpg")
    return new_url

if __name__ == "__main__":
    old_url = "https://scpic1.chinaz.net/files/default/imgs/2023-06-14/4230dbfa0c709e80_s.jpg"
    print(transform_url(old_url))  # 应该输出：https://tppic.chinaz.net/files/default/imgs/2023-06-14/4230dbfa0c709e80_big.jpg

