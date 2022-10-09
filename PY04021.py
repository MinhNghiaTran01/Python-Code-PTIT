import datetime
class Nguoi_choi:
    def __init__(self,ma_nguoi_choi,name,s,e):
        self.ma_nguoi_choi = ma_nguoi_choi
        self.name = name
        s = datetime.datetime.strptime(s, '%H:%M')
        e = datetime.datetime.strptime(e, '%H:%M')
        self.s = s
        self.e = e
        self.time = (e - s).total_seconds()
        self.h = self.time // 3600
        self.m = (self.time % 3600) // 60
    def __str__(self):
        return '{} {} {} gio {} phut'.format(self.ma_nguoi_choi,self.name,int(self.h),int(self.m))
a = []
n = int(input())
while n>0:
    n-=1
    a.append(Nguoi_choi(input(),input(),input(),input()))
a.sort(key = lambda x: (-x.time))
print(*a,sep='\n')