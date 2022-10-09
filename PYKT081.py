t = int(input())
while t>0:
    try:
        t-=1
        a = list(map(int,input().split('.')))
        check = True
        for i in range(len(a)):
            if a[i]<0 or a[i]>255:
                check = False
                break
        if check and len(a)==4:
            print("YES")
        else: print("NO")
    except:
        print("NO")