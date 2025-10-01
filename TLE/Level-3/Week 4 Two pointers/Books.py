n,t=map(int,input().split())
a=list(map(int,input().split()))
i=0
j=i
m=0
s=0
while i<len(a) and j<len(a):
    if s+a[j]<=t:
        s+=a[j]
        j+=1
        m=max(m,j-i)
    else:
        s-=a[i]
        i+=1 
print(m)


