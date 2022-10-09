while True:
    a = list(map(int,input().split()))
    check = 0
    for i in a:
        check = max(check,i)
    if check ==0: break
    cnt = 0
    while True:
        check = True
        b = a.copy()
        for i in range(3):
            if a[i] != a[i+1]:
                check = False
                break
        if check==True:
            print(cnt)
            break
        for i in range(3):
            a[i] = abs(b[i]-b[i+1])
        a[3] = abs(b[3]-b[0])
        cnt+=1