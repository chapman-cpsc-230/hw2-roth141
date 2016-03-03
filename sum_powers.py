# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 13:55:00 2016

@author: LydiaRoth
"""

b_str= raw_input("Enter a natural number")
b = int(b_str)
n = 1
i = 0
while i <= b:
    n += b**i
    print n,i 
    i = i +1
print "%.2f**(%d+1)/(%.2f-1)"%(b,n,b)
print "%.2f,%d" %(b,n)
     

  