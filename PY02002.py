t = int(input())
f = []
f.append(1)
f.append(1)
for i in range(2,94):
    f.append(0)
    f[i] = f[i-2] + f[i-1]
while t>0:
    t-=1
    a,b = map(int,input().split())
    for i in range(a,b+1):
        print(f[i-1],end=" ")
    print()