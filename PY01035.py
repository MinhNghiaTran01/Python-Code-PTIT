n = input()
n = n[::-1]
sum = 0
tmp = 1
for i in range(len(n)):
    if i>0:
        tmp*=2
    if n[i]=='1':
        sum+=tmp
print( oct(sum)[2::])