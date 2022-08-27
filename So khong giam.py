# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 16:02:15 2022

@author: Admin
"""

def so_khong_giam(n):
    for i in range(len(n)-1):
        if n[i] > n[i+1]:
            return 0
    return 1
t = int(input())
for i in range(t):
    n = input()
    if so_khong_giam(n):
        print('YES')
    else:
        print('NO')