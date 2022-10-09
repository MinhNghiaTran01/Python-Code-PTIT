t = int(input())
while t>0:
    t-=1
    n,b = map(int,input().split())
    ans = ""
    while n>0:
        mod = int(n%b)
        if mod>9:
           ans = chr(65 + mod - 10) + ans
        else: ans = chr( mod + 48) + ans
        n//=b
    print(ans)

