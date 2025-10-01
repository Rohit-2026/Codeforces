s = input().strip()
n = len(s)
a = [[] for l in range(26)]
for i in range(n):
    c = ord(s[i]) - ord('A')
    a[c].append(i + 1)
t = 0
for i in range(26):
    k = len(a[i])
    if k > 1:
        for j in range(k):
            t += a[i][j] * j + a[i][j] * (j - k + 1)
        t -= (k * (k - 1)) // 2
print(t)
