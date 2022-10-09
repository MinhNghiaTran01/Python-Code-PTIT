class so_phuc:
    def __init__(self,thuc,ao):
        self.thuc = thuc
        self.ao = ao
    def in_C(self,b):
        thuc = (self.thuc + b.thuc)
        ao = self.ao + b.ao
        tmp = thuc
        thuc = thuc*self.thuc - ao*self.ao
        ao = ao*self.thuc + tmp*self.ao
        dau = "+"
        if ao<0: dau = "-"
        print(thuc,dau,ao,end="")
        print("i, ",end="")
    def in_D(self,b):
        thuc =  self.thuc + b.thuc
        ao = self.ao + b.ao
        tmp = thuc
        thuc = thuc * thuc - ao*ao
        ao = tmp*ao + tmp*ao
        dau = '+'
        if ao<0: dau = '-'
        print(thuc,dau,ao,end="")
        print("i")

t = int(input())
while t>0:
    t-=1
    a = list(map(int,input().split()))
    sp1 = so_phuc(a[0],a[1])
    sp2 = so_phuc(a[2],a[3])
    sp1.in_C(sp2)
    sp1.in_D(sp2)