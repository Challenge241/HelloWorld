# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 16:40:01 2023

@author: Lenovo
"""
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
data={'Age':[14,16,18],
      'Height':[165,163,175],
      'is_tall':[1,0,1]}
data_frame=pd.DataFrame(data)
data_frame.head()
clf=LogisticRegression()
x=data_frame.drop('is_tall',axis=1)
y=data['is_tall']
clf.fit(x,y)
student4=[[19,176]]
clf.predict(student4)
svc=LinearSVC()
svc.fit(x,y)
svc.predict(student4)



