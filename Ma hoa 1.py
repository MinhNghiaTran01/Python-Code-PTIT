# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 16:14:36 2022

@author: Admin
"""

t = int(input())
for i in range(t):
    n = input()
    n+='_'
    i = 0
    cnt=1
    ans = ''
    while i<len(n)-1:
        if n[i] == n[i+1]:
            cnt+=1
        else:
             ans+= str(cnt) + n[i]
             cnt=1
        i+=1
    print(ans)   
            