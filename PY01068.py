a = []
n,k = map(int,input().split())
s = set(input().split())
s = list(s)
s.sort()
def Try(tmp,j,cnt):
    if cnt == k:
        a.append(tmp)
        return
    else:
        for i in range(j,len(s)):
            x = tmp
            tmp+=s[i] + " "
            Try(tmp,i+1,cnt+1)
            tmp=x
Try("",0,0)
print(*a,sep='\n')