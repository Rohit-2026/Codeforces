from collections import Counter
c = Counter(map(int, input().split()))
print(sum(v // 2 for v in c.values()))
