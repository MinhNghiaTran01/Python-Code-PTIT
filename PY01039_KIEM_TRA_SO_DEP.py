
t = int(input())
while t>0:
    t-=1
    a = set()
    n = input()
    check = True
    a.add(n[0])
    a.add(n[1])
    for i in range(2,len(n)):
        if(n[i]!=n[i-2]):
            check = False
        a.add(n[i])
    if check==True and len(a) == 2:
        print("YES")
    else:
        print("NO")
        