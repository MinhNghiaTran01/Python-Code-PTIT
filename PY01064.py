def Try(n,k,cnt):
    if n==k:
        return cnt
    else:
        if n//2>=k: return Try(n//2,k,cnt-1)
        else: return Try(n,k-n//2,cnt)

t = int(input())
while t>0:
    t-=1
    n,k = map(int,input().split())
    cnt = n
    n = pow(2,n)
    print(chr(Try(n,k,cnt)+65))
