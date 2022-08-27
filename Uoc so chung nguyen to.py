# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 15:45:09 2022

@author: Admin
"""
import math
def ucln(a,b):
    if b==0:
        return a
    else:
        return ucln(b, a%b)
def tong(n):
    _sum=0
    while n>0:
        _sum+=n%10
        n//=10
    return _sum
def snt(n):
    for i in range(2,math.isqrt(n)+1):
        if n%i==0:
            return 0
    return n>1
t =int(input())
for i in range(t):
    a,b = map(int,input().split())
    if snt(tong(ucln(a,b))):
        print('YES')
    else:
        print('NO')