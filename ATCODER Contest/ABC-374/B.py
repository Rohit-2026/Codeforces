s = input().strip()
s1 = input().strip()
n = min(len(s), len(s1))
for i in range(n):
    if s[i] != s1[i]:
        print(i + 1)
        break
else:
    if len(s) != len(s1):
        print(n + 1)
    else:
        print(0)
