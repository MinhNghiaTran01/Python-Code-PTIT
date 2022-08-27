# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 17:09:41 2022

@author: Admin
"""

t =int(input())
while t>0:
    t-=1
    s = input() 
    l  = len(s)
    if s[l-2]=='8' and s[l-1]=='6':
        print('YES')
    else:
        print('NO')
        
            