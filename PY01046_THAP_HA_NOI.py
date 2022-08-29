def println(a,c,b):
    print(a," -> ",c)
    
def recursive(a,b,c,n):
    if n==1:
        println(a, c, b)
    else:
        recursive(a, c, b, n-1)
        println(a, c, b)
        recursive(b, a, c , n-1)
n = int(input())
recursive('A', 'B', 'C', n)