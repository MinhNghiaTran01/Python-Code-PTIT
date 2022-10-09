while True:
    n = int(input())
    if n==0: break
    a = []
    for i in range(n):
        a.append(int(input()))
    tmp_min = min(a)
    tmp_max = max(a)
    if tmp_max==tmp_min:
        print("BANG NHAU")
    else:
        print(tmp_min,tmp_max)