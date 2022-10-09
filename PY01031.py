t = int(input())
while t>0:
    t-=1
    n,b = map(int,input().split())
    ans = ''
    while n>0:
        tmp = n%b
        if tmp>9:
            ans = chr(65+tmp-10) + ans
        else:
            ans =  chr(48+tmp) + ans
        n//=b
    print(ans)
