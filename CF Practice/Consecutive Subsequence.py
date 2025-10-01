n=int(input())
a=list(map(int,input().split()))
d={}
prev=[-1]*n
last={}
for i in range(n):
    v=a[i]
    if v-1 not in d:
        d[v]=1
    else:
        prev[i]=last[v-1]
        d[v]=d[v-1]+1
    last[v]=i
m=0
b=0
for i in d:
    if d[i]>m:
        m=d[i]
        b=i
print(m)
res=[]
cur=last[b]
while cur!=-1:
    res.append(cur+1)
    cur=prev[cur]
res.reverse()
print(*res)
