t = int(input())
while t>0:
    t-=1
    n = int(input())
    a = list(map(int,input().split()))
    stack = [-1]
    for i in range(n):
        if len(stack)==1:
            stack.append(i)
            print(1,end=" ")
        else:
            while len(stack)>1 and a[stack[len(stack)-1]] <= a[i]:
                stack.pop()
            print(i-stack[len(stack)-1],end=" ")
            stack.append(i)
    print()