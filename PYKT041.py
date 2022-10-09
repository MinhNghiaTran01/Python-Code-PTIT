n = int(input())
a = []
for i in range(n):
    tmp = input()
    a.append(tmp)
ans = 0
for i in range(n):
    hang = 0
    cot = 0
    for j in range(n):
        if a[i][j] == 'C':
            cot+=1
        if a[j][i] =='C':
            hang+=1
    if hang>0:
        ans+= ((hang-1)*hang)//2
    if cot>0:
        ans += ((cot - 1) * cot) // 2
print(ans)