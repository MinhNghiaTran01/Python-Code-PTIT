import math
def so_nguyen_to(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return n>1
n = int(input())
a = list(map(int,input().split()))
d = dict()
for i in a:
    if i in d:
        d[i]+=1
    elif so_nguyen_to(i):
        d[i] = 1
for i in a:
    if i in d:
        print(i,d[i])
        del d[i]

