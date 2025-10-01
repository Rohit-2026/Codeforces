n, p = map(int, input().split())
s = list(input())
q = [input().split() for i in range(p)]
q = [(int(x), l) for x, l in q]
c = 0
for i in range(n - 2):
    if s[i:i+3] == ['A', 'B', 'C']:
        c += 1
for x, l in q:
    x -= 1
    for i in range(x - 2, x + 1):
        if 0 <= i <= n - 3 and s[i:i+3] == ['A', 'B', 'C']:
            c -= 1
    s[x] = l
    for i in range(x - 2, x + 1):
        if 0 <= i <= n - 3 and s[i:i+3] == ['A', 'B', 'C']:
            c += 1
    print(c)
