
import math
def snt(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return 0
    return n>1
t = int(input())
while t>0:
    t-=1
    n = input()
    cnt = 0
    for i in range(len(n)):
        if n[i] == '2' or n[i] =='3' or n[i] =='5' or n[i]=='7':
            cnt+=1
        else:
            cnt-=1
    if cnt>0 and snt(len(n)):
        print("YES")
    else:
        print("NO")
