import math
t =int(input())
for i in range(t):
    n,x,m = map(float,input().split())
    x/=100
    x = 1+x
    n = m/n
    year = math.log(n,x)  
    print(math.ceil(year))
    