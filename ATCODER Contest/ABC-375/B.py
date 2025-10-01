import math
n = int(input())
a, b, t = 0, 0, 0
for i in range(n):
    x, y = map(int, input().split())
    t += math.sqrt((a - x) ** 2 + (b - y) ** 2)
    a, b = x, y
t += math.sqrt(a ** 2 + b ** 2)
print(t)
