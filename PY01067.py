a = []
def Try(s,cnt):
    if len(a)==1001:
        return
    if cnt>len(s)//2:
        a.append(s)
    for i in range(3):
        tmp = s
        s+= str(i)
        if i==2 : Try(s,cnt+1)
        else: Try(s,cnt)
        s = tmp
Try("2",0)
t = int(input())
while t>0:
    t-=1
    n = int(input())
    for i in range(n):
        print(a[i],end=" ")
    print()