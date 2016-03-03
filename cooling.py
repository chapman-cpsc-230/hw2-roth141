# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 23:13:51 2016

@author: LydiaRoth
"""

T = 100.0
L = 20.0
t = 0
while t<= L:
    T -= 0.055 *(T-L)
    print t,T
    t = t + 1
print "%d,%.2f" %(t,T)
