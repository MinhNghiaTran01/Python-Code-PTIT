# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 16:41:51 2022

@author: Admin
"""

t = int(input())
while t>0:
    t-=1
    s = input()
    giam = False
    check = True
    for i in range(1,len(s)):
        if s[i] < s[i-1] and giam == False:
            giam = True
        if s[i] > s[i-1] and giam == True or s[i] == s[i-1]:
            check = False
            break
    if check and len(s) >=3 :
         print("YES")
    else:
        print("NO")
         