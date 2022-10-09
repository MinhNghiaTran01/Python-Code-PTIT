t = int(input())
while t>0:
    t-=1
    n,m = map(int,input().split())
    a = []
    for i in range(n):
        tmp = list(map(int,input().split()))
        a.append(tmp)
    for i in range(n):
        for j in range(n):
            tmp = 0
            for k in range(m):
                tmp+=a[i][k]*a[j][k]
            print(tmp,end=" ")
        print()