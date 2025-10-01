from collections import deque
h,w=map(int,input().split())
g=[input() for i in range(h)]
s=t=None
for i in range(h):
    for j in range(w):
        if g[i][j]=='S':
            s=(i,j)
        elif g[i][j]=='G':
            t=(i,j)
v_moves=[(-1,0),(1,0)]
h_moves=[(0,-1),(0,1)]
vis=[[[False,False] for i in range(w)] for j in range(h)]
q=deque([(s[0],s[1],0,0),(s[0],s[1],1,0)])
vis[s[0]][s[1]][0]=True
vis[s[0]][s[1]][1]=True
while q:
    y,x,d,st=q.popleft()
    if (y,x)==t:
        print(st)
        exit()
    moves=h_moves if d==0 else v_moves
    for dy,dx in moves:
        ny,nx=y+dy,x+dx
        if 0<=ny<h and 0<=nx<w and g[ny][nx]!='#':
            if not vis[ny][nx][1-d]:
                vis[ny][nx][1-d]=True
                q.append((ny,nx,1-d,st+1))
print(-1)
