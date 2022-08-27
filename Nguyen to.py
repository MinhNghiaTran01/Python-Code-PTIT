import math
t = int(input())
def ucln(a,b):
    if b==0:
        return a
    else:
        return ucln(b,a%b)
def snt(n):
    for i in range(2,math.isqrt(n)+1):
        if n%i==0:
            return 0
    return n>1
for i in range(t):
    cnt=0
    n = int(input())
    for i in range(1,n):
        if ucln(n,i)==1:
            cnt+=1
    if snt(cnt):
        print('YES')
    else:
        print('NO')