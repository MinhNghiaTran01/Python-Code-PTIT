import math
n = int(input())
m = n
n = int(math.sqrt(n))
ans = 0
a = [0 for i in range(n+1)]
a[0] = 1
a[1] = 1
for i in range(2,int(math.sqrt(n)+1)):
    if a[i]==0:
        for j in range(i*i,n+1,i):
            a[j] = 1
snt = []
for i in range(2,len(a)):
    if a[i]==0:
        snt.append(i)

for i in range(2,int(math.sqrt(n))):
    x1 = i*i
    if i in snt:
        if i**8<m:
            ans+=1
        x2 = m//x1
        x2 = int(math.sqrt(x2))
        cnt1,cnt2 = 0,0
        for k in range(0,len(snt)+1):
            if snt[k] == i: cnt1 = k
            if snt[k] > x2:
                cnt2 = k-1
                break
        ans += cnt2 - cnt1
print(ans)

