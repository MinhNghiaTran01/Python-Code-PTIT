n = input()
if n[0]!='6':
    print("NO")
else:
    tmp_6 = n.count('6')
    tmp_68 = n.count('68')
    tmp_688 = n.count('688')
    cnt = (tmp_6-tmp_68) + (tmp_68-tmp_688)*2 + tmp_688*3
    if cnt==len(n):
        print("YES")
    else:
        print("NO")