# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 17:20:42 2022

@author: Admin
"""
def check(n):
    _sum=int(n[0])
    for i in range(1,len(n)-1):
        if abs(ord(n[i]) - ord(n[i-1]))!=2 :
            return 0
        _sum+=int(n[i])
    _sum+=int(n[len(n)-1])
    if _sum%10==0:
        return 1
    else:
        return 0
t =int(input())
while t>0:
    t-=1
    n = input()
    if check(n):
        print('YES')
    else:
        print('NO')
            