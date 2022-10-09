id = 1
class Nhan_vien:
    ma_thi_sinh = "TS"
    xep_loai = ""
    def __init__(self,name,diem_ly_thuyet,diem_thuc_hanh):
        global id
        self.ma_thi_sinh+="0"
        self.ma_thi_sinh+=str(id)
        id+=1
        while diem_thuc_hanh>10: diem_thuc_hanh/=10
        while diem_ly_thuyet>10: diem_ly_thuyet/=10
        self.name = name
        self.diem_ly_thuyet = diem_ly_thuyet
        self.diem_thuc_hanh = diem_thuc_hanh
        self.diem_trung_binh = (diem_ly_thuyet+diem_thuc_hanh)/2
        if self.diem_trung_binh>9.5: self.xep_loai = "XUAT SAC"
        elif self.diem_trung_binh>=8: self.xep_loai = "DAT"
        elif self.diem_trung_binh>=5: self.xep_loai = "CAN NHAC"
        else: self.xep_loai = "TRUOT"
    #def __str__(self):
        #pass
    def __repr__(self):
        return '{} {} {:.2f} {}'.format(self.ma_thi_sinh, self.name, self.diem_trung_binh, self.xep_loai)
a = []
n = int(input())
while n>0:
    n-=1
    a.append(Nhan_vien(input(),float(input()),float(input())))
a.sort(key = lambda x: (-x.diem_trung_binh))
print(*a,sep='\n')
