
import math
def snt(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return 0
    return n>1
t = int(input())
while t>0:
    t-=1
    s = input()
    if(len(s)<4):
        print("NO")
        continue
    s = s[(len(s)-4):len(s)]
    n = int(s)
    if snt(n):
        print("YES")
    else:
        print("NO")
    