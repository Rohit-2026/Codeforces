n=int(input())
a=list(map(int, input().split()))
b=a[:]
d=[0]*(n+1)
for i in range(n):
    d[i+1]+=d[i]
    b[i]+=d[i]
    if i+1<n:
        d[i+1]+=1
    if i+1+b[i]<n:
        d[i+1+b[i]]-=1
    b[i]=max(0,b[i]-(n-i-1))
print(*b)
