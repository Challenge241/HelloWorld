# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 10:11:58 2023

@author: Lenovo
"""

from bs4 import BeautifulSoup
import requests

# pip install beautifulsoup4

# soup对象
#  页面源码
# html.parser  解释器
# soup = BeautifulSoup(页面源码， 'html.parser'  )


url = "https://www.jxust.edu.cn/index/jlxw1.htm"
res = requests.get( url )
res.encoding = 'utf-8'

# 创建soup对象
soup = BeautifulSoup( res.text, 'html.parser')

"""
第一种方式
    soup.标签名称
    默认返回搜索到的标签第一个,没有找到返回None
"""
t1 = soup.title
print( t1 )
"""  
提取 标签里面的文本
"""
# <title> 文本   <span></span>  </title>
print( t1.string ) # 标签里面只能是文本内容，不能包含其他标签存在
print( t1.text )# 获取当前标签下的所有文本内容


"""
第二种定位方式
    soup.find()
    和第一种方式返回的结果是一样，默认返回第一个，没有返回None
    find( 标签名称  ,  attrs={'属性名称':'属性值'}  )
    find可以进行属性过滤
"""
meta = soup.find('meta', attrs={'name':'keywords'})
print( meta )

"""
在定位的标签中进行 提取属性
"""
#attrs 功能就是，展示
print( meta.attrs['content']  )
#bs4 在进行html.parser解释的时候，就已经把标签的属性解析成了字典格式
print( meta['content']   )
print( '='*100)


"""
第三种定位方式
    soup.find_all()
    返回所有找到的标签， []序列， 如果没有找到返回空的[]
    find_all( 标签名称,  attrs={属性名称:属性值 } )
"""
div = soup.find('div', attrs={'class':'left_box1'})
li_all = div.find_all('li')
for li in li_all:
    a = li.a
    print(  'https://www.jxust.edu.cn'+  a['href'][2:]    )
    print( a.string )
    print( a['title'])
    print('='*100)


soup.select() # 返回所有的获取到的标签
soup.select_one() #返回一个