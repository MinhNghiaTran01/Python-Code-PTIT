t = int(input())
while t>0:
    t-=1
    n, m = map(int,input().split())
    a = []
    kernel = []
    for i in range(n):
        tmp = list(map(int,input().split()))
        a.append(tmp)
    for i in range(3):
        tmp = list(map(int,input().split()))
        kernel.append(tmp)
    ans = 0
    for i in range(1,n-1):
        for j in range(1,m-1):
            sum = 0
            for k in range(0,3):
                for l in range(0,3):
                    sum+= a[i+k-1][j+l-1]*kernel[k][l]
            ans = ans + sum
    print(ans)