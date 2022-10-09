cnt = 1
class khach_hang:
    def __init__(self,ten_khach_hang,chi_so_cu,chi_so_moi):
        global cnt
        self.ten_khach_hang = ten_khach_hang
        self.chi_so_cu = chi_so_cu
        self.chi_so_moi = chi_so_moi
        self.ma_khach_hang = "KH"
        if cnt<10: self.ma_khach_hang+="0"
        self.ma_khach_hang+=str(cnt)
        cnt+=1
        s = chi_so_moi - chi_so_cu
        if s <= 50:
            s *= 100
            s += s * 0.02
        elif s <= 100:
            s = 50 * 100 + (s - 50) * 150
            s += s * 0.03
        else:
            s = 50 * 100 + 50 * 150 + (s - 100) * 200
            s += s * 0.05
        self.tong_tien = round(s)
n = int(input())
danh_sach_khach_hang = []
while n>0:
    n-=1
    k = khach_hang(input(),int(input()),int(input()))
    danh_sach_khach_hang.append(k)
danh_sach_khach_hang.sort(key = lambda x: -x.tong_tien)
for i in danh_sach_khach_hang:
    print('%s %s %s'%(i.ma_khach_hang,i.ten_khach_hang,i.tong_tien))