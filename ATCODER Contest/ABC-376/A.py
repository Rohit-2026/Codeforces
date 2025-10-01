n, c = map(int, input().split())
a = list(map(int, input().split()))
k = a[0]
cc = 1
for i in range(1, n):
    if a[i] - k >= c:
        cc += 1
        k = a[i]
print(cc)
