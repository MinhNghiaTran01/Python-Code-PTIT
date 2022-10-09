f = []
for i in range(10001):
    f.append(0)
for i in range(2,101):
    if f[i]==0:
        for j in range(i*i,10001,i):
            f[j] = 1
snt = []
for i in range(2,10000):
    if f[i]==0:
        snt.append(i)
n,x = map(int,input().split())
print(x,end=" ")
for i in range(0,n):
    print(x+snt[i],end= " ")
    x = x+ snt[i]