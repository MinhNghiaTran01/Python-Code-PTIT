n = int(input())
a = list(map(int,input().split()))
ans_so_buoc = 10**999
ans_value = a[0]
for i in range(n-1,-1,-1):
    so_buoc = 0
    for j in range(n):
        if j!=i:
            so_buoc+= abs(a[i]-a[j])
    if ans_so_buoc>=so_buoc:
        ans_so_buoc = so_buoc
        ans_value = a[i]
print(ans_so_buoc,ans_value)