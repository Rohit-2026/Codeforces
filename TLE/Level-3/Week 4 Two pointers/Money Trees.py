for i in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    i=0
    j=0
    c=0
    m=0
    while j<n:
        if i<j and b[j-1]%b[j]!=0:
            i=j
            c=a[j]
        else:
            c+=a[j]
        while c>k:
            c-=a[i]
            i+=1
        m=max(m,j-i+1)
        j+=1
    print(m)            