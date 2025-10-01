n=int(input())
a=list(map(int,input().split()))
d={}
b=[]
for i in range(n):
    if a[i] not in d:
        d[a[i]]=i+1
for i in range(n):
    if i>=d[a[i]]:
        b.append(d[a[i]])
        d[a[i]]=i+1
    else:
        b.append(-1)
print(*b)            