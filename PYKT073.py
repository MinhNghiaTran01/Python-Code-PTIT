n = int(input())
a = []
for i in range(n):
    tmp = input()
    a.append(tmp)
i = 0
ans = []
while i<n:
    tmp = a[i].split()
    if len(tmp)==6:
        i+=1
        so_luong_tu = 6
        while i<n:
            tmp = a[i].split()
            if (len(tmp)==6 and so_luong_tu==8) or (len(tmp)==8 and so_luong_tu==6): i+=1
            else: break
            so_luong_tu=len(tmp)
        ans.append(1)
    elif len(tmp)==7:
        cnt=0
        while i<n:
            tmp = a[i].split()
            if len(tmp)==7:
                cnt+=1
                i+=1
            if len(tmp)!=7 or cnt==4:
                break
        if cnt==4:
            ans.append(2)
print(len(ans))
print(*ans,sep='\n')

