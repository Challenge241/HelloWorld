# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 21:33:41 2023

@author: Lenovo
"""
link='www.baidu.com'
for i in range(1,3):
    link_a=link+"/{i}"
    link_b=link+"/{}"
    link_c=link+f"/{i}"
    print(link_a)
    print(link_b)
    print(link_b.format(i))
    print(link_c)
    print()