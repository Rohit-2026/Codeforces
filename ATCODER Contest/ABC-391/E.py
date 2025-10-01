import heapq

n, k = map(int, input().split())
a = sorted(map(int, input().split()), reverse=True)
b = sorted(map(int, input().split()), reverse=True)
c = sorted(map(int, input().split()), reverse=True)

# Precompute the top k sums using a max-heap
max_heap = []
heapq.heappush(max_heap, (-(a[0] * b[0] + b[0] * c[0] + c[0] * a[0]), 0, 0, 0))
seen = set()
seen.add((0, 0, 0))

result = []
while max_heap and len(result) < k:
    val, i, j, l = heapq.heappop(max_heap)
    result.append(-val)
    if i + 1 < n and (i + 1, j, l) not in seen:
        heapq.heappush(max_heap, (-(a[i + 1] * b[j] + b[j] * c[l] + c[l] * a[i + 1]), i + 1, j, l))
        seen.add((i + 1, j, l))
    if j + 1 < n and (i, j + 1, l) not in seen:
        heapq.heappush(max_heap, (-(a[i] * b[j + 1] + b[j + 1] * c[l] + c[l] * a[i]), i, j + 1, l))
        seen.add((i, j + 1, l))
    if l + 1 < n and (i, j, l + 1) not in seen:
        heapq.heappush(max_heap, (-(a[i] * b[j] + b[j] * c[l + 1] + c[l + 1] * a[i]), i, j, l + 1))
        seen.add((i, j, l + 1))

# The k-th largest sum is the last element in the result list
print(result[k - 1])