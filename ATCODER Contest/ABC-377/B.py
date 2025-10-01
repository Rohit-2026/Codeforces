r=set()
c=set()
g=[input() for _ in range(8)]
for i in range(8):
    for j in range(8):
        if g[i][j]=='#':
            r.add(i)
            c.add(j)
s=0
for i in range(8):
    for j in range(8):
        if g[i][j]=='.' and i not in r and j not in c:
            s+=1
print(s)
