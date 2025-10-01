n,s=map(int,input().split())
a=list(map(int,input().split()))
i=0
j=0
c=100000000
su=0
while j<n and i<n:
    if su+a[j]<s:
        su+=a[j]
        j+=1
    else:
        c=min(c,j-i+1)
        su-=a[i]
        i+=1    
if c==100000000:
    print(-1)
else:
    print(c)        
