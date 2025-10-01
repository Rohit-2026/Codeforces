for i in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort()
    c=1
    m=0
    if n==1:
        print(0)
        continue
    for i in range(1,n):
        if a[i]-a[i-1]<=k:
            c+=1
        else:
            c=1
        m=max(m,c)
    print(n-m)    
