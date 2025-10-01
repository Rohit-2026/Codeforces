n=int(input())
a=list(map(int,input().split()))
d={}
for x in a:
    d[x]=d.get(x,0)+1
k=sorted(d.keys())
p=[0]*len(k)
p[0]=d[k[0]]
for i in range(1, len(k)):
    p[i]=p[i-1]+d[k[i]]
c=0
for x in a:
    h=x//2
    l=0
    r=len(k)-1
    while l<=r:
        m=(l+r)//2
        if k[m]<=h:
            l=m+1
        else:
            r=m-1
    if r>=0:
        c+=p[r]
print(c)
