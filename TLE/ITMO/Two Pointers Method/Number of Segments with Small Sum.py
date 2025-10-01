n,k=map(int,input().split())
a=list(map(int,input().split()))
j=1
c=0
if a[0]<=k:
    s=a[0]
else:
    s=0    
for i in range(n):
    if a[i]>k:
        continue
    else:
        s-=a[i]   
    while j<n:
        if s+a[j]<=k:
            s+=a[j]
            j+=1
        else:
            break
    c+=j-i
    print(i,j,c,s)
print(c)        


