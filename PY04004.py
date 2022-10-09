import math
class Fraction:
    def __init__(self,tu,mau):
        self.tu = tu
        self.mau = mau
    def toi_gian(self,ps):
        self.tu = self.tu*ps.mau + ps.tu*self.mau
        self.mau = self.mau*ps.mau
        gcd = math.gcd(self.tu, self.mau)
        return '{}{}{}'.format(int(self.tu/gcd),"/",int(self.mau/gcd))
a = list(map(int,input().split()))
ps1 = Fraction(a[0],a[1])
ps2 = Fraction(a[2],a[3])
print(ps1.toi_gian(ps2))