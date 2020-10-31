# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 15:30:06 2020

@author: cad
"""


def pythonsum(n):
    a = range(n)
    print(a)
    b = range(n)
    print(b)
    c = []
    for i in range(len(a)):
        a[i] = i ** 2
        b[i] = i ** 3
        c.append(a[i] + b[i])
    print(c)
    return c


pythonsum(10)