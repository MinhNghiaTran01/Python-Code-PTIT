from decimal import Decimal,ROUND_HALF_UP
cnt = 1
class Sinh_Vien:
    def __init__(self,ho_ten,p):
        global cnt
        self.ma_hoc_sinh = "HS"
        self.ma_hoc_sinh+='{:02d}'.format(cnt)
        cnt+=1
        self.ho_ten = ho_ten
        self.p = p
        sum=0
        for i in range(len(p)):
            if i<=1:
                sum+=p[i]*2
            else: sum+=p[i]
        self.diem_trung_binh = sum/12
        if self.diem_trung_binh>=9: self.xep_loai = "XUAT SAC"
        elif self.diem_trung_binh>=8: self.xep_loai ="GIOI"
        elif self.diem_trung_binh>=7: self.xep_loai = "KHA"
        elif self.diem_trung_binh>=5: self.xep_loai = "TB"
        else: self.xep_loai = "YEU"
        sum/=12
        self.diem_trung_binh = sum.quantize(Decimal('0.1'),ROUND_HALF_UP)
n = int(input())
danh_sach_sinh_vien = []
while n>0:
    n-=1
    sv = Sinh_Vien(input(),list(map(Decimal,input().split())))
    danh_sach_sinh_vien.append(sv)
danh_sach_sinh_vien.sort(key = lambda x: (-x.diem_trung_binh,x.ma_hoc_sinh))
for i in danh_sach_sinh_vien:
    print('%s %s %.1f %s' % (i.ma_hoc_sinh, i.ho_ten, i.diem_trung_binh, i.xep_loai))