# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 17:32:37 2022

@author: Admin
"""
n = input()
ans = ''
for i in range(len(n)-1,0,-1):
    if i%3==0:
        ans = ',' + n[i] + ans
    else:
        ans = n[i] + ans
ans = n[0] + ans
print(ans)
            