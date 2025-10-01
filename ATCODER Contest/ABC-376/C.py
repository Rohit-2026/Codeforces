n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
l, h = 1, max(a)
a.sort(reverse=True)
while l < h:
    m = (l + h) // 2
    x = b + [m]
    x.sort(reverse=True)
    f = True
    for i in range(n):
        if a[i] > x[i]:
            f = False
            break
    if f:
        h = m
    else:
        l = m + 1
x = b + [l]
x.sort(reverse=True)
f = True
for i in range(n):
    if a[i] > x[i]:
        f = False
        break
if f:
    print(l)
else:
    print(-1)
