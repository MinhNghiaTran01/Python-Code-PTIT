import math
def kt_nt(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return n>1
n,m = map(int,input().split())
a = [[]]
for i in range(n):
    tmp = list(map(int,input().split()))
    a.append(tmp)
for i in a:
    for j in i:
        if kt_nt(j): print(1,end= " ")
        else: print(0,end=" ")
    print()