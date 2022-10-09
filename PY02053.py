n = int(input())
a = []
for i in range(n):
    tmp = list(map(int,input().split()))
    a.append(tmp)
sum_tren_duong_cheo_phu = 0
sum_duoi_duong_cheo_phu = 0
for i in range(n):
    for j in range(n):
        if j<(n-i-1): sum_tren_duong_cheo_phu += a[i][j]
        elif j>(n-i-1): sum_duoi_duong_cheo_phu+= a[i][j]
k = int( input())
if abs(sum_tren_duong_cheo_phu-sum_duoi_duong_cheo_phu)<=k:
    print("YES")
else:
    print("NO")
print(abs(sum_tren_duong_cheo_phu-sum_duoi_duong_cheo_phu))

