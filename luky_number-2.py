def lucky_number(n):
    while n>0:
        if n%10!=4 and n%10!=7:
            return 0
        n//=10
    return 1
t = int(input())
for i in range(t):
    n = int(input())
    if lucky_number(n):
        print('YES')
    else:
        print('NO')