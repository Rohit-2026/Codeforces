n, m = map(int, input().split())
a = [[] for o in range(n + 1)]
v = [None] * (n + 1)
for o in range(m):
    x, y, w = map(int, input().split())
    a[x].append((y, w))
    a[y].append((x, -w))
def f(start, x):
    stack = [(start, x)]
    while stack:
        u, val = stack.pop()
        if v[u] is None:
            v[u] = val
            for n, w in a[u]:
                if v[n] is None:
                    stack.append((n, val + w))
for i in range(1, n + 1):
    if v[i] is None:
        f(i, 0)
print(*v[1:])
