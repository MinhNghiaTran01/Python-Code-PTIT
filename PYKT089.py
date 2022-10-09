n = int(input())
a = []
while n>0:
    tmp = list(map(int,input().split()))
    for i in tmp:
        a.append(i)
    n-=len(tmp)
chan = []
le = []
for i in range(len(a)):
    if a[i]%2==0:
        chan.append(a[i])
        a[i] = 0
    else:
        le.append(a[i])
        a[i] = 1
chan.sort()
le.sort(reverse=True)
cnt_chan = 0
cnt_le = 0
for i in range(len(a)):
    if a[i]==0:
        print(chan[cnt_chan],end=" ")
        cnt_chan+=1
    else:
        print(le[cnt_le],end=" ")
        cnt_le+=1

