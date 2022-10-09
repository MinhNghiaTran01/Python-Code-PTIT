n = int(input())
ans = {}
key = ""
value = 0
while n>0:
    line = input()
    if len(line)==0:
        ans[key] = value
        key = ""
        value = 0
    if key=="":
        key = line
    else: value+=1
    n-=1
if key!="":
    ans[key] = value
for k,v in ans.items():
    k+=":"
    print(k,v)
