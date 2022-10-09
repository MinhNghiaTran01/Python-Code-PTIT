t = int(input())
while t>0:
    t-=1
    n = int(input())
    a = list(map(int,input().split()))
    d = {}
    for i in a:
        d.setdefault(i,0)
        d[i]+=1
    for k,v in d.items():
        if v%2!=0:
            print(k)
            break
