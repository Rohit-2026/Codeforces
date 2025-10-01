n, *data = map(int, open(0).read().split())
qrs, Q, idx= data[:2 * n], data[2 * n], 0
queries = data[2 * n + 1:]
for i in range(Q):
    t, d = queries[2 * i] - 1, queries[2 * i + 1]
    q, r = qrs[2 * t], qrs[2 * t + 1]
    rem = d % q
    nxt = d if rem == r else d + (r - rem if rem < r else q - rem + r)
    print(nxt)
