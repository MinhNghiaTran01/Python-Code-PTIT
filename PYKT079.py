t = int(input())
while t>0:
    t-=1
    n = int(input())
    a = set(map(int,input().split()))
    smallest = min(a)
    biggest = max(a)
    print(biggest-smallest-len(a)+1)