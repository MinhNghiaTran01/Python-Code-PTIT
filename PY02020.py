n = int(input())
a = list(map(float,input().split()))
a.sort()
ans = 0;
tmp_min = a[0]
tmp_max = a[len(a)-1]
cnt = 0
for i in range(0,len(a)):
    if a[i]!=tmp_max and a[i]!=tmp_min:
        ans+=a[i]
        cnt+=1
ans/= cnt
print("%.2f" % ans)