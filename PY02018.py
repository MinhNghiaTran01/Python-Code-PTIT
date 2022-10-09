n = int(input())
a = list(map(int,input().split()))
a.sort()
ans = -1
for i in range(1,len(a)):
    if a[i] - 1 > a[i-1]:
        ans = a[i-1] + 1;
        break
if ans==-1:
    print(a[len(a)-1]+1)
else:
    print(ans)
