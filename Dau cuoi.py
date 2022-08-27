t = int(input())
for i in range(t):
    a = input()
    if a[0]== a[len(a)-2] and a[1] == a[len(a)-1]:
        print('YES')
    else:
        print('NO')