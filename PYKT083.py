n = int(input())
loai_xe = { "Xe_con_5": 10000,"Xe_con_7":15000,"Xe_tai_2":20000,"Xe_khach_29":50000,"Xe_khach_45":70000}
thong_ke = {}
while n>0:
    n-=1
    a = list(map(str,input().split()))
    thong_ke.setdefault(a[4],0)
    if a[3] == "IN":
        xe = a[1] + "_" + a[2]
        thong_ke[a[4]] = thong_ke.get(a[4])  + loai_xe[xe]
for k,v in thong_ke.items():
    k+=":"
    print(k,v)