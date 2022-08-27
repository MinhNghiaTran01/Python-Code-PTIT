n = int(input())
cnt=0
while n>0:
    mod = n%10
    if mod == 4 or mod== 7:
        cnt+=1
    n//=10
if cnt== 4 or cnt==7:
    print('YES')
else:
    print('NO')