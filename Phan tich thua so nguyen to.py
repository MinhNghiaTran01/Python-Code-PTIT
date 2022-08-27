# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 17:12:08 2022

@author: Admin
"""
import math

t =int(input())
while t>0:
    t-=1
    n = int(input())
    ans = '1 * '
    for i in range(2,math.isqrt(n)+1):
        cnt=0
        while n%i==0:
            n//=i
            cnt+=1
        if cnt>0:
            ans+= str(i) + '^' + str(cnt)
            if n>1:
                ans+= ' * '
    if n>1:
        ans += str(n) + '^' +'1'
    print(ans)
        
            