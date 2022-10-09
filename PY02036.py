n = int(input())
a = []
for i in range(n):
    tmp = list(map(int,input().split()))
    a.append(tmp)
sum_tren_duong_cheo_chinh = 0
sum_duoi_duong_cheo_chinh = 0
for i in range(n):
    for j in range(n):
        if j>i: sum_tren_duong_cheo_chinh += a[i][j]
        elif j<i: sum_duoi_duong_cheo_chinh+= a[i][j]
k = int(input())
if abs(sum_tren_duong_cheo_chinh-sum_duoi_duong_cheo_chinh)<=k:
    print("YES")
else:
    print("NO")
print(abs(sum_tren_duong_cheo_chinh-sum_duoi_duong_cheo_chinh))

