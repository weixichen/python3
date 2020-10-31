# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 17:20:53 2020

@author: cad
"""
import datetime as dt
import numpy as np
n = 200000
A,B = [],[]
start = dt.datetime.now()
for i in range(n):
    A.append(i ** 2)
    B.append(i ** 3)
c = []
for a,b in zip(A,B):
    c.append(a + b)
print((dt.datetime.now() - start).microseconds)
    
#numpy

start = dt.datetime.now()
c = np.arange(n) ** 2 + np.arange(n) ** 3
print((dt.datetime.now() - start).microseconds)

