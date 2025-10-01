n,m=map(int,input().split())
g=[[]for i in range(n)]
for i in range(m):
    u,v,w=map(int,input().split())
    u-=1
    v-=1
    g[u]+=[(v,w)]
    g[v]+=[(u,w)]
a=float('inf')
s=[(0,0,{0})]
while s:
    v,x,p=s.pop()
    if v==n-1:
        a=min(a,x)
    for u,w in g[v]:
        if u not in p:
            s.append((u,x^w,p|{u}))
print(a)
