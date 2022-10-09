import math
snt = [0]*10001
b = []
for i in range(2,10001):
    if snt[i]==0:
        for j in range(i*i,10001,i): snt[j]=1
        b.append(i)

n = int(input())
a = list(map(int,input().split()))
a.sort(reverse=True)
ans = 0
for i in range(n):
    if a[i] not in b:
        for j in range(len(b)):
            if b[j]>=a[i]:
                index = j
                break
        if index==0:
            ans = abs(b[index]-a[i])
        else: ans=max(min(abs(b[index]-a[i]),abs(b[index-1]-a[i])),ans)
print(ans)