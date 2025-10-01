n=int(input())
a=list(map(int,input().split()))
i=1
c=0
a.sort()
while i<n:
    if a[i]>a[i-1]:
        a[i],a[i-1]=a[i-1],a[i]
        i+=2
    else:
        i+=1
for i in range(1,n,2):
    if a[i]>a[i-1] and a[i]>a[i+1]:
        c+=1    
print(c)
print(*a)            
