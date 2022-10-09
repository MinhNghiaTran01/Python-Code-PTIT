n,m = map(int,input().split())
a = []
dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]
for i in range(n):
    tmp = list(map(int,input().split()))
    a.append(tmp)
ans = 0
visit = [[False for y in range(m+1)] for x in range(n+1)]
for i in range(n):
    for j in range(m):
        if a[i][j] == -1:
            for k in range(8):
                ix = i + dx[k]
                iy = j + dy[k]
                if ix>=0 and ix<n and iy>=0 and iy<m and visit[ix][iy]==False:
                    ans+=a[ix][iy]
                    visit[ix][iy] = True
print(ans)
