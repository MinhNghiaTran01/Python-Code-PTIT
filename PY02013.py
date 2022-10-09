while True:
    n = int(input())
    if n==0: break
    cnt = 1
    if n==1:
        print(1)
        continue
    while True:
        cnt+=1
        if n%2==0: n//=2
        else: n = n*3+1
        if n == 1: break
    print(cnt)
        
        