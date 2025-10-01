n=int(input())
a=list(map(int,input().split()))
d={} 
i={}  
for q,x in enumerate(a):
    d[x]=d.get(x,0)+1
    i[x]=q+1 
m=-1
c=-1
for x in d:
    if d[x]==1 and x>m:
        m=x
        c=i[x]
print(c)
