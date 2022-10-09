t = int(input())
i = 1
while i<=t:
    s1 = input()
    s2 = input()
    tmp = " "
    s1 = list(tmp.join(s1).split())
    s2 = list(tmp.join(s2).split())
    s1.sort()
    s2.sort()
    if s1==s2:
        print("Test",(str(i)+":"),"YES")
    else:
        print("Test", (str(i) + ":"), "NO")
    i+=1