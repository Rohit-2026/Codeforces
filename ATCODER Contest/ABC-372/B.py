M = int(input())
p = [3**i for i in range(11)]
a = []
for i in range(10, -1, -1):
    while M >= p[i]:
        M -= p[i]
        a.append(i)
n = len(a)
print(n)
print(*a)
