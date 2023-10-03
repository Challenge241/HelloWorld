# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 14:51:26 2023

@author: Lenovo
"""
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
import numpy as np
x,y=make_blobs(centers=4,random_state=18)
y=y%2
plt.scatter(x[:,0],x[:,1],c=y,s=80,cmap='autumn',edgecolor='k')
plt.show()

from mpl_toolkits.mplot3d import Axes3D,axes3d
figure=plt.figure()
x_new=np.hstack([x,x[:,1:]**2])
ax=Axes3D(figure,elev=-152,azim=26)
mask=y==0
ax.scatter(x_new[mask,0],x_new[mask,1],x_new[mask,2],c='r',s=80)
ax.scatter(x_new[~mask,0],x_new[~mask,1],x_new[~mask,2],c='b',marker='*',s=80)
plt.show()

