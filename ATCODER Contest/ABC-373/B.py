s = input()
p = [0] * 26
for i in range(26):
    p[ord(s[i]) - 65] = i
d = 0
c = p[0]
for x in range(1, 26):
    d += abs(p[x] - c)
    c = p[x]
print(d)
