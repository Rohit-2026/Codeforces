n,s=map(int,input().split())
a=list(map(int,input().split()))
i=0
j=0
c=0
su=0
while j<n and i<n:
    if su+a[j]<=s:
        su+=a[j]
        c=max(c,j-i+1)
        j+=1
    else:
        su-=a[i]
        i+=1    
print(c)        
