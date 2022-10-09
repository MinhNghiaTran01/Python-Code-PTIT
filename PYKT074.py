t = int(input())
while t>0:
    t-=1
    tmp = input().split()
    cnt = 0
    ans = []
    for i in range(len(tmp)):
        cnt+=len(tmp[i])
        if cnt<=100:
            ans.append(tmp[i])
        else:
            break
        cnt+=1
    print(*ans)