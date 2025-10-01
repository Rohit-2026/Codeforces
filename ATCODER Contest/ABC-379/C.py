n, m = map(int, input().split())
x = list(map(int, input().split()))
a = list(map(int, input().split()))
if sum(a) != n:
    print(-1)
else:
    s_map, c = {}, 0
    for i in range(m):
        s_map[x[i]] = s_map.get(x[i], 0) + a[i]
    for i in range(1, n):
        if i in s_map:
            e = s_map[i] - 1
            if e> 0:
                s_map[i] = 1
                s_map[i + 1] = s_map.get(i + 1, 0) + e
                c += e
    print(c if s_map.get(n, 0) == 1 else -1)
