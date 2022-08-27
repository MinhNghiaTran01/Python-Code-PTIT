# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 16:28:19 2022

@author: Admin
"""
P = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'
while True:
    s = input() 
    if s=='0':
        break
    k,s = map(str,s.split())
    k = int(k)
    ans=''
    for i in range(len(s)):
        lc = P.index(s[i])
        ans = P[(lc+k)%28] + ans
    print(ans)
        
            