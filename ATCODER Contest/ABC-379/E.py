n = int(input().strip())
s = input().strip()
cs = int(s[0])
ts = cs
for i in range(1, n):
    cs = cs * 10 + (i + 1) * int(s[i])
    ts += cs
print(ts)
