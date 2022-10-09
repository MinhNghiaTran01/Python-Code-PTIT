a = ['.','?','!']
tmp=""
while True:
    try:
        s = list(map(str,input().split()))
    except:
        break
    for i in range(len(s)):
        for j in range(len(s[i])):
            if s[i][j] in a:
                if len(tmp)==0:
                    continue
                tmp = tmp.strip()
                tmp = tmp.lower()
                for k in range(len(tmp)):
                    if k==0:
                        print(tmp[0].upper(),end="")
                    else: print(tmp[k],end="")
                tmp = ""
                print()
            else: tmp+=s[i][j]
        tmp+=" "


