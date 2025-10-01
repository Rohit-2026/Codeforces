n = int(input())
a = list(map(int, input().split()))
t = []
l = [0] * n
for i in range(n - 1, -1, -1):
    l[i]+= len(t)
    while t and a[i] >t[-1]:
        t.pop()
    t.append(a[i])
print(*l)