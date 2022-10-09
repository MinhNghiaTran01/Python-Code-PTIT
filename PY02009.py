t = int(input())
while t>0:
    t-=1
    n = int(input())
    a = []
    tan_suat = {}
    for i in range(n):
        a.append(int(input()))
        if a[i] in tan_suat:
            tan_suat[a[i]] +=1
        else:
            tan_suat[a[i]] = 1
    tan_suat = dict(sorted(tan_suat.items(),key = lambda x: (-x[1],x[0])))
    ans = 0
    for key,value in tan_suat.items():
        ans = key
        break
    print(ans)
            
        
        