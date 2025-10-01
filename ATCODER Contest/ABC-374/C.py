n=int(input())
arr=list(map(int,input().split()))
m = float('inf')
for x in range(1 << n):
    a, b = 0, 0
    for i in range(n):
        if x & (1 << i):
            a += arr[i]
        else:
            b += arr[i]
    m = min(m, max(a, b))
print(m)
