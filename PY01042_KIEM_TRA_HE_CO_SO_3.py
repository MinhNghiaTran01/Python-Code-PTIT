

t = int(input())
while t>0:
    t-=1
    s = input()
    check = True
    for i in range(len(s)):
        if s[i]!='0' and s[i] != '1' and s[i] !='2':
            check = False
    if check:
        print("YES")
    else:
        print("NO")