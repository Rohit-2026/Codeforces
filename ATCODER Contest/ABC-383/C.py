from collections import deque
h,w,d=map(int,input().split())
grid=[input().strip() for i in range(h)]
visited=[[False] * w for i in range(h)]
queue=deque()
for i in range(h):
    for j in range(w):
        if grid[i][j]=='H':
            queue.append((i,j,0))
            visited[i][j]=True
while queue:
    x,y,dist=queue.popleft()
    if dist<d:
        for dx,dy in [(-1, 0),(1, 0),(0, -1),(0, 1)]:
            nx,ny=x+dx,y+dy
            if 0<=nx<h and 0<=ny<w and not visited[nx][ny] and grid[nx][ny] != '#':
                visited[nx][ny]=True
                queue.append((nx,ny,dist+1))
count=sum(visited[i][j] for i in range(h) for j in range(w) if grid[i][j] != '#')
print(count)
