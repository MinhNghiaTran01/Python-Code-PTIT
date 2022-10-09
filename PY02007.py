a = []
while len(a)<10:
    b = list(map(int,input().split()))
    for i in b:
       a.append(i)
ans = set()
for i in a:
    ans.add(i%42)
print(len(ans))
