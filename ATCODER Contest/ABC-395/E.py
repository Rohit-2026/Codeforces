import sys, heapq
input = sys.stdin.readline

# Read input values
N, M, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
revGraph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    revGraph[v].append(u)

INF = 10**18
# dist[0][v] is min cost to reach v in original orientation,
# dist[1][v] is min cost to reach v in reversed orientation.
dist = [[INF] * (N + 1) for _ in range(2)]
dist[0][1] = 0

# Priority queue: (current cost, vertex, parity)
pq = [(0, 1, 0)]
while pq:
    cost, v, parity = heapq.heappop(pq)
    if cost != dist[parity][v]:
        continue
    if v == N:
        print(cost)
        sys.exit(0)
    # Operation 1: move along an edge (cost 1)
    if parity == 0:
        for nxt in graph[v]:
            if cost + 1 < dist[0][nxt]:
                dist[0][nxt] = cost + 1
                heapq.heappush(pq, (dist[0][nxt], nxt, 0))
    else:
        for nxt in revGraph[v]:
            if cost + 1 < dist[1][nxt]:
                dist[1][nxt] = cost + 1
                heapq.heappush(pq, (dist[1][nxt], nxt, 1))
    # Operation 2: reverse the orientation (toggle parity, cost X)
    new_parity = 1 - parity
    if cost + X < dist[new_parity][v]:
        dist[new_parity][v] = cost + X
        heapq.heappush(pq, (dist[new_parity][v], v, new_parity))

print(min(dist[0][N], dist[1][N]))
