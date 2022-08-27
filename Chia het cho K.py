# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 15:49:40 2022

@author: Admin
"""

import math
a,k,n = map(int,input().split())
j = a//k
check=False
while True:
    if k*j>a and k*j<=n:
        print(k*j-a,end=' ')
        check=True
    if k*j>=n:
        break
    j+=1
if check==False:
    print(-1)