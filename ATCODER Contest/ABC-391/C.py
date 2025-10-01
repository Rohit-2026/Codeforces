n,q=map(int,input().split())
nest={i:1 for i in range(1,n+1)}
pigeon={i:i for i in range(1,n+1)}
c=0
r=[]
for l in range(q):
    x=list(map(int,input().split()))
    if x[0]==1:
        p,h=x[1],x[2]
        o=pigeon[p]
        nest[o]-=1
        if nest[o]==1:
            c-=1
        if nest.get(h,0)==1:
            c+=1
        nest[h]=nest.get(h,0)+1
        pigeon[p]=h
    else:
        print(str(c))
