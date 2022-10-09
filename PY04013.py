import datetime
a = {}
class Tram_Mua:
    def __init__(self,ten_tram,s,e,luong_mua):
        self.ten_tram = ten_tram
        self.s = s
        self.e = e
        self.luong_mua = luong_mua

n = int(input())
while n>0:
    n-=1
    x = Tram_Mua(input(),input(),input(),int(input()))
    s = datetime.datetime.strptime(x.s, '%H:%M')
    e = datetime.datetime.strptime(x.e, '%H:%M')
    h = (e - s).total_seconds()
    h = h / 3600
    if x.ten_tram in a:
        a[x.ten_tram][0] += x.luong_mua
        a[x.ten_tram][1] +=  h
    else:
        a[x.ten_tram] = [x.luong_mua,h]
cnt = 1
for k,v in a.items():
    ma_tram_do = "T"
    if cnt<10: ma_tram_do+="0"
    ma_tram_do+= str(cnt)
    #print(v[0],v[1])
    luong_mua_trung_binh = v[0]/v[1]
    print("%s %s %.2f"%(ma_tram_do,k,luong_mua_trung_binh))
    cnt+=1