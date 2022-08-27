# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 09:04:17 2022

@author: Admin
"""


a = input()
upperr,lowerr = 0,0
for i in a:
    if i.isupper():
        upperr+=1
    else:
        lowerr+=1
if upperr > lowerr:
    print(a.upper())
else:
    print(a.lower())      
