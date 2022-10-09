import math
class Fraction:
    def __init__(self,tu,mau):
        self.tu = tu
        self.mau = mau
    def toi_gian(self):
        gcd = math.gcd(self.tu,self.mau)
        self.tu = self.tu/gcd
        self.mau = self.mau/gcd
        return '{}{}{}'.format(int(self.tu),"/",int(self.mau))
tu,mau = map(int,input().split())
f = Fraction(tu,mau)
print(f.toi_gian())