# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 16:06:01 2022

@author: Admin
"""
t = int(input())
for i in range(t):
    n = input()
    ans=''
    for i in range(0,len(n),2):
        cnt = int(n[i+1])
        while cnt>0:
            ans+=n[i]
            cnt-=1
    print(ans)