n,d=map(int,input().split())
t,l=[],[]
for i in range(n):
    x,y=map(int,input().split())
    t.append(x)
    l.append(y)
for k in range(1,d+1):
    m=0
    for i in range(n):
        m=max(m,t[i]*(l[i]+k))
    print(m)
