for p in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    t=[0]*n
    for i in range(1,n-1):
        if a[i]>a[i-1] and a[i]>a[i+1]:
            t[i]=1
    l=0
    c=sum(t[1:k-1])
    m=c
    for i in range(1,n-k+1):
        if t[i+k-2]==1:
            c+=1  
        if t[i]==1:
            c-=1 
        if c>m:
            l=i
            m=c
    print(m+1,l+1)     





















