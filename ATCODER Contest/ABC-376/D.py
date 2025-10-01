from collections import deque
n, m = map(int, input().split())
adj = [[] for i in range(n+1)]
for i in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
q = deque([(1, 0)])
dist = [-1] * (n+1)
dist[1] = 0
min_cycle = float('inf')
while q:
    curr, d = q.popleft()
    for next in adj[curr]:
        if next == 1:
            min_cycle = min(min_cycle, d + 1)
        if dist[next] == -1:
            dist[next] = d + 1
            q.append((next, d + 1))
print(min_cycle if min_cycle != float('inf') else -1)
