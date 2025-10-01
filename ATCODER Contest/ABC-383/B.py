from itertools import combinations
h,w,d=map(int,input().split())
g=[input().strip()for p in range(h)]
f=[(i,j)for i in range(h)for j in range(w)if g[i][j]=="."]
m=0
for h1,h2 in combinations(f,2):
    s=set()
    for i in range(h):
        for j in range(w):
            if g[i][j]=="."and(abs(i-h1[0])+abs(j-h1[1])<=d or abs(i-h2[0])+abs(j-h2[1])<=d):
                s.add((i,j))
    m=max(m,len(s))
print(m)
