
def check(s):
    for i in range(len(s)//2):
        if s[i] != s[len(s)-i-1]:
            return 0
    return 1

def so_thuan_nghich(ans,n,a):
    if len(ans)>0 and len(ans)%2==0 and ans[0] !='0' and check(ans):
        tmp = int(ans)
        a.append(tmp)
        
    for i in range(0,9,2):
        tmp = ans
        if i==0 and len(ans)==0 :
            continue
        ans += str(i)
        if(int(ans)<n):
            so_thuan_nghich(ans, n,a)
        else:
            break
        ans = tmp
t = int(input())
while t>0:
    t-=1
    n = int(input())
    ans = ""
    a = []
    so_thuan_nghich(ans,n,a)
    a.sort()
    for i in a:
        print(i,end=' ')
    print()
        