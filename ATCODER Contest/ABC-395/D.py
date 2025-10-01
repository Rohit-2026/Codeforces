n,q=map(int,input().split())
p=list(range(n+1))
l=list(range(n+1))
r=list(range(n+1))
for i in range(q):
    f=input().split()
    if f[0]=="1":
        a=int(f[1])
        b=int(f[2])
        p[a]=l[b]
    elif f[0]=="2":
        a=int(f[1])
        b=int(f[2])
        x=l[a]
        y=l[b]
        l[a],l[b]=y,x
        r[x],r[y]=b,a
    else:
        a=int(f[1])
        print(str(r[p[a]]))
