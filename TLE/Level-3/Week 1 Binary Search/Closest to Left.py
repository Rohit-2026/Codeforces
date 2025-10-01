n,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
for i in b:
    l=0
    h=n-1
    r=0
    while l<=h:
        mid=(l+h)//2
        if a[mid]<=i:
            l=mid+1
            r=mid
        else:
            h=mid-1  
    if h>-1:
        print(r+1)
    else:
        print(0)               
