# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 16:49:45 2022

@author: Admin
"""
P = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'
def check(s,rs):
    for i in range(1,len(s)):
        if abs(ord(s[i])-ord(s[i-1]))!=abs(ord(rs[i])-ord(rs[i-1])):
            return 0
    return 1
t =int(input())
while t>0:
    t-=1
    s = input() 
    rs = s[::-1]
    if check(s,rs):
        print('YES')
    else:
        print('NO')
        
            