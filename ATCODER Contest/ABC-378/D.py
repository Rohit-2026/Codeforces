def dfs(x, y, s):
    global c
    if s == K:
        c += 1
        return
    v.add((x, y))
    for dx, dy in d:
        nx, ny = x + dx, y + dy
        if 0 <= nx < H and 0 <= ny < W and g[nx][ny] == '.' and (nx, ny) not in v:
            dfs(nx, ny, s + 1)
    v.remove((x, y))
H, W, K = map(int, input().split())
g = [input().strip() for i in range(H)]
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
c= 0
for i in range(H):
    for j in range(W):
        if g[i][j] == '.':
            v = set()
            dfs(i, j, 0)
print(c)
