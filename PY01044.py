a = set(input().lower().split())
b = set(input().lower().split())
tmp_1 = list(a.union(b))
tmp_2 = list(a.intersection(b))
tmp_1.sort()
tmp_2.sort()
print(*tmp_1)
print(*tmp_2)
