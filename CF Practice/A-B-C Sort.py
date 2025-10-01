for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    k=sorted(a)
    if n%2==0:
        for i in range(0,n,2):
            if a[i]>a[i+1]:
                a[i],a[i+1]=a[i+1],a[i]
        if k==a:
            print("YES")
        else:
            print("NO")            
    else:
        for i in range(1,n,2):
            if a[i]>a[i+1]:
                a[i],a[i+1]=a[i+1],a[i]
        if k==a:
            print("YES")
        else:
            print("NO")              
                          