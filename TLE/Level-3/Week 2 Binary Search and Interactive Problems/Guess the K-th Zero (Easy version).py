import sys
n, t = map(int, input().split())
sys.stdout.flush()
k = int(input())
sys.stdout.flush()
l = 0
h = n - 1
for _ in range(20):
    m = (l + h) // 2
    print("?", 1, m + 1)
    sys.stdout.flush()
    j = int(input())
    if j == -1:
        break
    if m + 1 - j >= k:
        h = m
    else:
        l = m + 1
print("!", l + 1)
sys.stdout.flush()
