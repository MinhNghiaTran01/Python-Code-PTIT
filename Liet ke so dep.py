# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 09:08:21 2022

@author: Admin
"""
def palindrome(n):
    n =str(n)
    tmp = str(n)
    n = n[::-1]
    return n == tmp
def check(n):
    cnt=0
    while n>0:
        mod = n%10
        if mod%2!=0:
            return 0
        n//=10
        cnt+=1
    return cnt
t = int(input())
for i in range(t):
    n =int(input())
    for i in range(22,n,2):
        cnt=check(i)
        if cnt:
            if cnt%2==0 and palindrome(i):
                print(i,end=' ')
    print()