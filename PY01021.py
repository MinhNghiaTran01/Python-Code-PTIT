t = int(input())
while t>0:
    t-=1
    s = input()
    sum = 0
    ans = ""
    for i in s:
        i = str(i)
        if i.isnumeric():
            sum+= int(i)
        else: ans+=i
    ans = list(ans)
    ans.sort()
    print(*ans,sum,sep="")