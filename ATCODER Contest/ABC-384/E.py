from collections import deque

# Input parsing
H, W, X = map(int, input().split())
P, Q = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(H)]

# Adjust for 0-based indexing
P -= 1
Q -= 1

# Initialize BFS
visited = set()
queue = deque([(P, Q)])
visited.add((P, Q))
strength = grid[P][Q]

# Directions for adjacency
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# BFS
while queue:
    x, y = queue.popleft()
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < H and 0 <= ny < W and (nx, ny) not in visited:
            # Check the absorption condition
            if grid[nx][ny]*X <strength:
                # Absorb slime
                strength += grid[nx][ny]
                visited.add((nx, ny))
                queue.append((nx, ny))
        

# Output the final strength
print(strength)
