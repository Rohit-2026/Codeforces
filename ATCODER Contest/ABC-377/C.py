n, m = map(int, input().split())
p = [tuple(map(int, input().split())) for l in range(m)]
d = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
c = set()
for a, b in p:
    c.add((a, b))
    for da, db in d:
        na, nb = a + da, b + db
        if 1 <= na <= n and 1 <= nb <= n:
            c.add((na, nb))
print(n**2 - len(c))
