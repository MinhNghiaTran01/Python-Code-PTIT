n = input()
while len(n)%3!=0:
    n = "0" + n
a = [4,2,1]
ans = ""
i=0
while i<len(n)-2:
    sum=0
    j=0
    while j<3:
        if n[i]=='1':
            sum+=a[j]
        i+=1
        j+=1
    ans+=str(sum)
print(ans)