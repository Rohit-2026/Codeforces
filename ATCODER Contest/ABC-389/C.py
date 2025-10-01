from collections import deque
n=int(input())
q=[input().split() for i in range(n)]
d=deque()
o=0
r=[]
for c in q:
    if c[0]=='1':
        l=int(c[1])
        if d:
            d.append((d[-1][0]+d[-1][1],l))
        else:
            d.append((0,l))
    elif c[0]=='2':
        o+=d.popleft()[1]
    else:
        k=int(c[1])-1
        print(d[k][0]-o)
