# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 22:01:32 2023

@author: Lenovo
"""

import numpy as np

a = np.array([1, 2, 3])
b = np.array([2, 1, 4])
c=np.array([2, 1, 4])
result = np.greater(a, b)
print(result)  # [False  True False]
print(np.equal(a.all, b.all))
print(np.equal(b.all,c.all))
if False not in (b==c):
    print(True)
