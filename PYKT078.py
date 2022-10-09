t = int(input())
while t>0:
    t-=1
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    am = []
    duong = []
    for i in range(n):
        if a[i]<0:
            am.append(a[i])
        else:
            duong.append(a[i])
    print(*am,end=" ")
    big = max(duong)
    for i in range(len(duong)):
        if duong[i]== big:
            print(k,duong[i],end=" ")
        else:
            print(duong[i],end=" ")
    print()
